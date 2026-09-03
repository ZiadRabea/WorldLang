from.model import *

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [word for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return np.array(bag)


def detect(text):
    inp = text
    bow = bag_of_words(inp, words)
    
    input_data = np.array([bow], dtype=np.float32) 

    results = model.predict(input_data)
    results_index = np.argmax(results)

    tag = labels[results_index]

    return tag
