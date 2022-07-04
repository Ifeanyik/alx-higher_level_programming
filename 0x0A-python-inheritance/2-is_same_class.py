#!/usr/bin/python3
'''Type checking function'''


def is_same_class(obj, a_class):
    '''function that verifies object type'''
    if type(obj) is a_class:
        return True
    else:
        return False
