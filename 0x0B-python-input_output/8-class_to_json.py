#!/usr/bin/python3
'''Module that returns the dictionary description
of an objects attributes'''


import json


def class_to_json(obj):
    '''Returns dictionary description of object attributes'''
    man = json.dumps(obj.__dict__)
    return json.loads(man)
