#!/usr/bin/python3
'''Module that loads JSON object from file'''


import json


def load_from_json_file(filename):
    '''Function that reads JSON object from a file'''
    with open(filename, "r", encoding="utf-8") as myFile:
        return json.load(myFile)
