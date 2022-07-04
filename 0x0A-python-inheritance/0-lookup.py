#!/usr/bin/python3
'''Create a function'''


def lookup(obj):
    '''Returns list of object attributes'''
    ma_list = list()
    if obj is None:
        return ma_list
    for i in obj.__dict__:
        ma_list.append(i)
    return ma_list
