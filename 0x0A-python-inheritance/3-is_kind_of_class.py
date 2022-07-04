#!/usr/bin/python3
'''Function to check subclasses'''


def is_kind_of_class(obj, a_class):
    '''Checks if obj is instance or subclass of a_class'''
    if isinstance(a_class, obj):
        return True
    return issubclass(MyList, list)
