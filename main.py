import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif get_close_matches(w, data.keys(), cutoff=0.8):
        ans = input(
            "Did you mean: %s? Enter Y for yes or N for no: " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if ans == "Y" or "y":
            # TODO: figure out why this return line breaks the program
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif ans == "N" or "n":
            return "Try again"
        else:
            return "Error"
    else:
        return "Word not found."


word = input("Enter word: ")

print(definition(word))
