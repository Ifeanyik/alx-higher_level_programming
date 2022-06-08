#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a = True if key in a_dictionary else False
    if a:
        a_dictionary[key] = value
        return a_dictionary
    else:
        a_dictionary[key] = value
    return a_dictionary
