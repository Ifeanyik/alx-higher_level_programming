#!/usr/bin/python3
'''Defining module functions'''


import json


def save_to_json_file(my_obj, filename):
    '''Writes JSON object to file'''
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
