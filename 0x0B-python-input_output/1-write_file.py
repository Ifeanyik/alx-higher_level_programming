#!/usr/bin/python3
'''Defining module'''


def write_file(filename="", text=""):
    '''Writes to a file and returns number of characters written'''
    with open(filename, mode="w") as myFile:
        chars = myFile.write(text)
    return chars
