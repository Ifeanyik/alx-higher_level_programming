#!/usr/bin/python3
'''Defining module functions'''


import json


def save_to_json_file(my_obj, filename):
    '''Writes JSON object to file'''
    obj = json.dumps(my_obj)
    with open(filename, mode="w") as myFile:
        myFile.write(obj)
