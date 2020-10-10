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


        words.append(word.split())


    print(words)





