#!/usr/bin/python3
'''Defining module'''


def append_write(filename="", text=""):
    '''writes to file and returns number of characters written'''
    with open(filename, mode="a") as myFile:
        chars = myFile.write(text)
    return chars
