#!/usr/bin/python3
'''Defining module functions'''


import json


def from_json_string(my_str):
    '''Convert JSON object to Python object'''
    return json.loads(my_str)
