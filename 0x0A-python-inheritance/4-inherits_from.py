#!/usr/bin/python3
'''Function to check subclasses'''


def inherits_from(obj, a_class):
    '''Checks if obj is instance or subclass of a_class'''
    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
