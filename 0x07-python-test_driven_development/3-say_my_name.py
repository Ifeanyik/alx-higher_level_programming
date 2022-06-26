#!/usr/bin/python3
'''Function that prints strings supplied to it in a sentence'''
def say_my_name(first_name, last_name=""):
    '''Prints given strings and raises typeerror if type other than string is given'''
    if type(first_name) != str or type(last_name) != str:
        raise TypeError("first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
