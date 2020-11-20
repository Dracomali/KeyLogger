import os
import sys

words = []
clnwrd = []


# checks for apostrophes
def apostro(value):
    if value == '\'':
        return True

    else:
        return False


# removes nesting lists
def nonest(x, newlist):
    for y in x:
        for z in y:
             newlist.append(str(z))

    return newlist        
            
# opens file
with open('/home/l3phant/PycharmProjects/Ckeylogger/Datat.txt', 'r') as data:

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

            if "Key.space" in word:
                words.append(word.split("Key.space"))

        else:
            words.append(word.split("Key."))


nonest(words, clnwrd)
idx = 0

for thing in clnwrd:
    if "space\n" in thing:
        del clnwrd[idx]
    
    if "Key.space" in thing:
        clnwrd[idx].split("Key.space")
         
    if "Key.shift" in thing:
        clnwrd[idx].split("Key.shift")

    if thing == '':
        del clnwrd[idx]
    
    idx += 1

print(clnwrd)


