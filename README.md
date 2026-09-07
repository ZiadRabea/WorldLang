# WorldLang

<p align="center">
  <img src="images/world.png" alt="WorldLang Logo" width="200">
</p>

<p align="center">
  <strong>English</strong> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.zh.md">中文</a> |
  <a href="README.ja.md">日本語</a>
</p>

**A multilingual programming language that lets you write, run, detect, and translate code in your native language.**

<p align="center">
  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="GitHub License">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="VSCode Extension">
  </a>
  <br>
  <a href="https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation">
    <img src="https://img.shields.io/badge/ResearchGate-preprint-brightgreen" alt="ResearchGate">
  </a>
</p>

**Resources & Links:**

* 📖 **[Official Documentation](https://ziadrabea.github.io/WorldDocs)**

  * 🚀 [Getting Started](https://ziadrabea.github.io/WorldDocs/installation.html)
  * 📚 [Language Reference](https://ziadrabea.github.io/WorldDocs/features.html)
  * 🌍 [Supported Languages](https://ziadrabea.github.io/WorldDocs/languages.html)
  * 🤝 [Contributing Guide](https://ziadrabea.github.io/WorldDocs/guide.html)
* 🌐 **[Official Website](https://ziadrabea.github.io/worldlanguage)**
* 💬 **[Join the Community](https://flow.daisyscript.com)**
* 🔬 **[Academic Pre-print (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
* 🧩 **[WorldLangEN VS Code Extension](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
* 👤 **Maintainer:** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [Email](mailto:zidr2005@gmail.com))

WorldLang is an open-source interpreter built in Python that removes the language barrier in programming. Instead of requiring programmers to write using English keywords, WorldLang allows code to be written using native-language syntax.

The interpreter supports a multilingual execution pipeline built around a custom **Lexer → Parser → Runtime** architecture, along with automatic language detection and integrated source-to-source code translation.

> **Supported languages: 31** — Arabic, Azerbaijani, Chinese, Dutch, English, Finnish, French, German, Greek, Indonesian, Irish, Italian, Japanese, Kazakh, Korean, Kurdish, Latvian, Malay, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Swedish, Turkish, Ukrainian, Urdu, Uzbek, Vietnamese, and Hindi.

---

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Language Detection & Selection](#language-detection--selection)
* [Code Translation](#code-translation)
* [Code Example](#code-example)
* [Built-in Libraries](#built-in-libraries)
* [Architecture](#architecture)
* [Language & Library Management](#language--library-management)
* [Contributing](#contributing)
* [License](#license)

---

## Features

* **Native-language programming** — write code using the keywords of your chosen language.
* **31 supported language packs** with dynamically loaded keyword mappings.
* **Hybrid language selection** — manually select a language or allow WorldLang to detect it automatically.
* **AI-based language detection** — automatically detect the programming language syntax before lexing when no language is manually selected.
* **Cross-language execution** — run files written in different supported languages without manually switching the global language.
* **Integrated code translation** — translate WorldLang source files between supported languages.
* **Dynamic keyword mapping** — the lexer maps native keywords to generic tokens on the fly.
* **Full-featured interpreter** — variables, functions, recursion, loops, conditionals, lists, dictionaries, and arithmetic.
* **Hardware & robotics** — serial communication for microcontrollers such as Arduino.
* **Speech** — text-to-speech and voice recognition.
* **Built-in libraries** — image processing, plotting, random utilities, filesystem tools, and more.
* **Generative AI** — optional Google Gemini integration.
* **Library & extension management** — fetch `.world` libraries and extensions directly from the network.

---

## Requirements

* **Python 3.12+**
* **Windows, macOS, or Linux**

Core packages:

| Package               | Used for                                                |
| --------------------- | ------------------------------------------------------- |
| `requests`            | Downloading language packs, libraries, and extensions   |
| `numpy`               | AI language detection and numerical processing          |
| `keras`               | AI-based language detection                             |
| `nltk`                | Language detection preprocessing                        |
| `Pillow`              | Image processing (`_builtins/Image.py`)                 |
| `matplotlib`          | Plotting (`_builtins/Graph.py`)                         |
| `pyautogui`           | Mouse/keyboard control (`_builtins/Controls.py`)        |
| `pyserial`            | Serial/hardware communication (`_builtins/Serial.py`)   |
| `pyttsx3`             | Text-to-speech (`_builtins/Speech.py`)                  |
| `SpeechRecognition`   | Voice recognition (`_builtins/Speech.py`)               |
| `google-generativeai` | Generative AI (`_builtins/GenAI.py`)                    |
| `rich`                | Markdown rendering for AI output (`_builtins/GenAI.py`) |

> Only `requests` is required for the basic interpreter. `Keras`, `NLTK`, and `NumPy` are required for AI-based automatic language detection. Other packages are required only for their corresponding optional built-in libraries.

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/ZiadRabea/WorldLang.git
cd WorldLang

# 2. (Recommended) Create and activate a virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate

# 3. Install dependencies
pip install requests numpy keras nltk Pillow matplotlib pyautogui pyserial pyttsx3 SpeechRecognition rich
```

To enable Google Gemini AI features:

```bash
pip install google-generativeai
```

---

## Usage

The interpreter ships as a REPL (Read–Eval–Print Loop). To start it:

```bash
python bin/World.py
```

A prompt appears:

```text
World >>
```

Type a program and press Enter to execute it.

### Special Commands

| Command       | Action                                                               |
| ------------- | -------------------------------------------------------------------- |
| `world()`     | Run WorldLang Source Files                                           |
| `libman`      | Run the library manager and download `.world` libraries              |
| `langman`     | Run the language manager and download language packs                 |
| `extman`      | Run the extension manager and download extensions                    |
| `setlang`     | Manually select a programming language or enable automatic detection |
| `translate()` | Translate WorldLang source code between supported languages          |

---

## Language Detection & Selection

WorldLang supports a **hybrid language-selection system**.

You can explicitly select the language you want to use, or leave the language unset and allow the interpreter to automatically detect the language of the source code.

### Manual Language Selection

Use:

```text
setlang
```

Example:

```text
setlang -> ArabicKW
```

This manually configures WorldLang to use the Arabic keyword table.

### Automatic Language Detection

Leave the language input blank:

```text
setlang -> ""
```

This enables automatic language detection.

When automatic detection is enabled, WorldLang analyzes the source code and determines the appropriate language during the lexing/tokenizing phase.

This allows code and imported modules written in different supported languages to run **without manually switching the active language beforehand**.

### AI Detection Modules

The automatic language detection system uses:

* `Keras`
* `NLTK`
* `NumPy`

The detection system is optional when manually selecting a language with `setlang`.

---

## Code Translation

WorldLang includes an integrated **cross-language code translator**.

Instead of translating code using simple text replacement, the translator processes the source through a structured multilingual pipeline:

```text
Source
   ↓
Lexer
   ↓
Translator
   ↓
DeLexer
   ↓
Translated Source
```

The source code is first lexed into language-independent representations. The translator then maps those representations to the target language before the **DeLexer** reconstructs valid WorldLang source code.

### Translate Command

```text
translate(filename.world, source_language, target_language)
```

Example:

```text
translate("factorial.world", "English", "Chinese")
```

WorldLang automatically generates a translated source file using the target language.

For example:

```text
factorial_Chinese.world
```

This makes it possible to write a WorldLang program in one language and convert the same source code into another supported language.

---

## Code Example

The following factorial calculator can be written in Arabic:

```worldlang
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(الرقم))
```

The same program can also be written in English:

```worldlang
# Factorial Calculator
var number = int(input("Enter a number:"))

func factorial(number)
    if number == 1 or number == 0 do return 1
    return number * factorial(number - 1)
end

print(factorial(number))
```

When automatic detection is enabled, WorldLang can determine which supported language the source code uses without requiring a manual language change.

---

## Built-in Libraries

The interpreter exposes several Python-backed libraries, registered as native WorldLang functions:

| Library    | Purpose                                                                    | Backing module          |
| ---------- | -------------------------------------------------------------------------- | ----------------------- |
| `String`   | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ...              | `_builtins/String.py`   |
| `Random`   | Random number generation                                                   | `_builtins/Random.py`   |
| `os`       | Filesystem operations: `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py`       |
| `Image`    | Load/save images and convert to/from RGB lists                             | `_builtins/Image.py`    |
| `Graph`    | `plot`, `scatter`, `bar` charting                                          | `_builtins/Graph.py`    |
| `Controls` | Mouse/keyboard automation                                                  | `_builtins/Controls.py` |
| `Serial`   | Hardware/Arduino serial communication (`send`/`receive`)                   | `_builtins/Serial.py`   |
| `Speech`   | Text-to-speech and voice recognition                                       | `_builtins/Speech.py`   |
| `GenAI`    | Generative AI via Google Gemini                                            | `_builtins/GenAI.py`    |

---

## Architecture

WorldLang is a **tree-walking interpreter** with an extended multilingual processing architecture.

### Code Execution Pipeline

```text
Source Code
    ↓
Language Selection / AI Detection
    ↓
Lexer
    ↓
Tokens
    ↓
Parser
    ↓
Abstract Syntax Tree
    ↓
Runtime
    ↓
Result
```

The language detection layer allows WorldLang to dynamically determine which keyword table should be used before tokenization when no language has been manually selected.

### Code Translation Pipeline

```text
Source
   ↓
Lexer
   ↓
Language-Independent Representation
   ↓
Translator
   ↓
DeLexer
   ↓
Translated Source
```

This architecture allows WorldLang to execute and translate multilingual source code while keeping the underlying interpreter pipeline language-independent.

### Key Components

| File / Component | Role                                                                              |
| ---------------- | --------------------------------------------------------------------------------- |
| `World.py`       | Entry point and REPL shell                                                        |
| `Lexer.py`       | Tokenizer; dynamically maps keywords from the detected or selected language table |
| `Parser.py`      | Grammar rules and AST generation                                                  |
| `Interpreter.py` | Executes the AST and provides the standard library                                |
| `Tokens.py`      | Token types and keyword handling                                                  |
| `Translator.py`  | Converts tokenized source representations between supported languages             |
| `DeLexer.py`     | Reconstructs source code using the target language's keyword mappings             |
| `Errors.py`      | Error types (`IllegalChar`, `Syntax`, `Runtime`)                                  |
| `RT_result.py`   | Runtime results, contexts, and symbol tables                                      |
| `datatypes/`     | `Value`, `Number`, `String`, `List`, `Dict`, `Function`                           |
| `_builtins/`     | Python-backed standard libraries                                                  |
| `data/`          | Language keyword tables and multilingual language resources                       |

The keyword tables are data-driven JSON files, allowing additional languages to be added without rewriting the core interpreter grammar.

---

## Language & Library Management

WorldLang can fetch resources from the network at runtime:

* **`langman`** — download keyword tables for additional languages into `data/`.
* **`libman`** — download `.world` libraries.
* **`extman`** — download extensions into `extensions/`.
* **`setlang`** — manually configure a language or enable AI-based automatic language detection.
* **`translate()`** — convert WorldLang source files between supported languages.

> Language detection and translation operate on the multilingual keyword architecture, allowing different language packs to share the same underlying interpreter.

---

## Contributing

WorldLang is open-source and community-driven. Contributions are welcome in many forms:

* **Language contributors** — add or improve localization and keyword tables.
* **Compiler developers** — improve the lexer, parser, translator, DeLexer, runtime, and standard library.
* **AI developers** — improve automatic language detection models and preprocessing.
* **Hardware developers** — expand hardware and robotics integrations.
* **Testers** — discover bugs and improve reliability.
* **Everyone** — report issues, improve documentation, and share ideas.

To contribute:

1. Fork the repository.
2. Clone your fork and create a branch.
3. Make your changes and commit them.
4. Open a Pull Request to the `main` branch.

---

## License

WorldLang is released under the [MIT License](LICENSE).
