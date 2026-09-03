import numpy as np
import random
import json
import pickle
import keras
import sys
import nltk
import os
import re
import unicodedata
from collections import Counter
from keras import layers


# =========================
# Paths
# =========================

if getattr(sys, "frozen", False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))


DATA_VERSION = 2


# =========================
# Language data
# =========================

def load_languages():
    with open(
        os.path.join(app_path, "langs.json"),
        encoding="utf-8"
    ) as file:
        return json.load(file)


# =========================
# Source preprocessing
# =========================

STRING_RE = re.compile(
    r"""
    "(?:\\.|[^"\\])*"
    |
    '(?:\\.|[^'\\])*'
    |
    `(?:\\.|[^`\\])*`
    """,
    re.VERBOSE | re.DOTALL
)


COMMENT_RE = re.compile(
    r"""
    //.*?$
    |
    \#.*?$
    |
    /\*.*?\*/
    """,
    re.VERBOSE | re.MULTILINE | re.DOTALL
)


def normalize_source(source):
    """
    Unicode normalization without destroying non-Latin scripts.
    """
    return unicodedata.normalize("NFKC", source).casefold()


def remove_garbage(source):
    """
    Remove content that should have essentially zero
    influence on language identification.
    """

    # Remove strings first.
    source = STRING_RE.sub(" ", source)

    # Remove comments.
    source = COMMENT_RE.sub(" ", source)

    # Normalize Unicode.
    source = normalize_source(source)

    return source


# =========================
# Vocabulary building
# =========================

def build_vocabulary(data):
    """
    Build one global vocabulary directly from langs.json.

    Nothing is added from the source code itself.
    """

    vocabulary = set()

    for language in data["langs"]:
        for pattern in language["patterns"]:
            vocabulary.add(
                unicodedata.normalize("NFKC", pattern).casefold()
            )

    return sorted(
        vocabulary,
        key=len,
        reverse=True
    )


def is_cjk_token(token):
    """
    Chinese / Japanese / Korean patterns often appear without
    whitespace, so they need slightly different matching.
    """

    for char in token:
        code = ord(char)

        if (
            0x4E00 <= code <= 0x9FFF      # CJK
            or 0x3400 <= code <= 0x4DBF   # CJK Extension A
            or 0x3040 <= code <= 0x30FF   # Japanese
            or 0xAC00 <= code <= 0xD7AF   # Korean
            or 0x1100 <= code <= 0x11FF   # Hangul Jamo
        ):
            return True

    return False


# =========================
# Keyword extraction
# =========================

def extract_language_tokens(source, vocabulary):
    """
    Extract ONLY tokens that exist in langs.json.

    Everything else is ignored:
        - identifiers
        - numbers
        - operators
        - brackets
        - punctuation
        - arbitrary words
        - strings
        - comments
    """

    source = remove_garbage(source)

    extracted = []

    # -------------------------
    # 1. Normal word matching
    # -------------------------

    normal_patterns = [
        re.escape(word)
        for word in vocabulary
        if not is_cjk_token(word)
    ]

    if normal_patterns:
        normal_regex = re.compile(
            r"(?<!\w)(?:"
            + "|".join(normal_patterns)
            + r")(?!\w)",
            re.UNICODE
        )

        extracted.extend(
            match.group(0)
            for match in normal_regex.finditer(source)
        )

    # -------------------------
    # 2. CJK : Chinese / Japanese / Korean
    # -------------------------
    #
    # These languages can work without spaces.
    #
    # Example:
    #
    # 如果x打印(값)
    #
    # "如果" and "打印" can still be recognized.
    #

    cjk_patterns = [
        re.escape(word)
        for word in vocabulary
        if is_cjk_token(word)
    ]

    if cjk_patterns:
        cjk_regex = re.compile(
            "(?:" + "|".join(cjk_patterns) + ")"
        )

        extracted.extend(
            match.group(0)
            for match in cjk_regex.finditer(source)
        )

    return extracted


# =========================
# Training data preparation
# =========================

def prepare_data(data):
    vocabulary = build_vocabulary(data)

    labels = []
    documents = []

    for language in data["langs"]:

        tag = language["tag"]

        if tag not in labels:
            labels.append(tag)

        for pattern in language["patterns"]:

            tokens = extract_language_tokens(
                pattern,
                vocabulary
            )

            documents.append(
                (tokens, tag)
            )

    vocabulary = sorted(vocabulary)
    labels = sorted(labels)

    # Fast lookup.
    vocabulary_index = {
        word: index
        for index, word in enumerate(vocabulary)
    }

    training = []
    output = []

    for tokens, tag in documents:

        counts = Counter(tokens)

        # ------------------------------------
        # Frequency-limited representation
        # ------------------------------------
        #
        # We DON'T want a giant file containing:
        #
        # print print print print print...
        #
        # to overwhelm everything else.
        #
        # Maximum contribution = 4.
        #

        bag = np.zeros(
            len(vocabulary),
            dtype=np.float32
        )

        for token, count in counts.items():

            index = vocabulary_index.get(token)

            if index is None:
                continue

            bag[index] = min(count, 4) / 4.0

        training.append(bag)

        output_row = [
            0
            for _ in range(len(labels))
        ]

        output_row[
            labels.index(tag)
        ] = 1

        output.append(output_row)

    return (
        vocabulary,
        labels,
        np.array(training, dtype=np.float32),
        np.array(output, dtype=np.float32)
    )


# =========================
# Data cache
# =========================

def load_or_prepare_data():

    cache_path = os.path.join(
        app_path,
        "data.pickle"
    )

    try:
        with open(cache_path, "rb") as f:
            cached = pickle.load(f)

        # New cache format.
        if (
            isinstance(cached, dict)
            and cached.get("version") == DATA_VERSION
        ):
            print("Processed training data loaded.")
            return (
                cached["words"],
                cached["labels"],
                cached["training"],
                cached["output"]
            )

    except Exception:
        pass

    print(
        "Preparing multilingual training data..."
    )

    data = load_languages()

    words, labels, training, output = prepare_data(
        data
    )

    cache = {
        "version": DATA_VERSION,
        "words": words,
        "labels": labels,
        "training": training,
        "output": output
    }

    with open(cache_path, "wb") as f:
        pickle.dump(
            cache,
            f,
            protocol=pickle.HIGHEST_PROTOCOL
        )

    print(
        f"Processed {len(words)} language patterns."
    )

    return (
        words,
        labels,
        training,
        output
    )


# =========================
# Model
# =========================

def create_model(training, output):

    model = keras.Sequential([
        layers.Input(
            shape=(training.shape[1],)
        ),

        layers.Dense(
            32,
            activation="relu"
        ),

        layers.Dense(
            32,
            activation="relu"
        ),

        layers.Dense(
            16,
            activation="relu"
        ),

        layers.Dense(
            len(output[0]),
            activation="softmax"
        )
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


def load_or_train_model(training, output):

    model_path = os.path.join(
        app_path,
        "model.keras"
    )

    model = create_model(
        training,
        output
    )

    try:

        model = keras.models.load_model(
            model_path
        )

        print(
            "Model loaded successfully!"
        )

    except Exception:

        print(
            "No saved model found. "
            "Training a new one..."
        )

        model.fit(
            training,
            output,
            epochs=100,
            batch_size=8,
            verbose=1,
            shuffle=True
        )

        model.save(model_path)

        print(
            "Model trained and saved!"
        )

    return model


# =========================
# Global model
# =========================

words, labels, training, output = (
    load_or_prepare_data()
)

data = load_languages()

model = load_or_train_model(
    training,
    output
)