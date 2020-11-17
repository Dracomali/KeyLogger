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
                # adds words to the list
                word += str(character)

        # splits words by selected character
        if "Key.shift" in word:
            words.append(word.split("Key.shift"))

        else:
            words.append(word.split("Key."))

    data.close()

# Iterates through word list
for item in words:
    for thing in item:

        # cleans up list and tries to join nested values
        if "space\n" in thing or "Key.space" in thing:
            del words[item]["space\n"]

print(words)

