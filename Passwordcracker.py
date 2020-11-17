import os
import sys

words = []


# checks for apostrophes
def apostro(value):
    if value == '\'':
        return True

    else:
        return False


# opens file
with open('Datat.txt', 'r') as data:

    for line in data:
        word = ""

        for character in line:
            # skips apostrophes
            if character == '\'':
                pass

            else:
                word += str(character)

        if "Key.shift" in word:
            words.append(word.split("Key.shift"))

        else:
            words.append(word.split("Key."))

    data.close()

for item in words:
    for thing in item:
        if "space\n" in thing or "Key.space" in thing:
            del words[item][thing]

print(words)

