#!/usr/bin/python3
'''Module that returns the dictionary description
of an objects attributes'''


def class_to_json(obj):
    '''Returns dictionary description of object attributes'''
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}
