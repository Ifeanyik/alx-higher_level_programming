#!/usr/bin/python3
'''function to read a text file'''


def read_file(filename=""):
    '''reads a text file and prints to stdout'''
    with open(filename) as myFile:
        file1 = myFile.read()
        print(file1, end="")
