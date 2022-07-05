#!/usr/bin/python3
'''Defining module functions'''


import json
def to_json_string(my_obj):
    '''Convert python object to JSON string'''
    obo = dict()
    return json.dumps(my_obj, obo)
