import os
import sys

def clean(file_name):

    with open(file_name, 'r+') as file:

        list_of_data = [line.split("Key.shift") for line in file]

        for x in list_of_data:
            for y in x:
                y.split("\\'")

        print(list_of_data)

        file.close()



raw_file = "D:\Programming\python\Keylogger-Passwordcracker\Raw_Datat.txt"


clean(raw_file)