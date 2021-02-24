import json

data = json.load(open("data.json"))


def definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "Word not found."


word = input("Enter word: ")

print(definition(word))
