#!/usr/bin/python3
'''Defining module functions'''


import json


def to_json_string(my_obj):
    '''Convert python object to JSON string'''
    return json.dumps(my_obj)
