#!/usr/bin/python3
'''Create a function'''


def lookup(obj):
    '''Returns list of object attributes'''
    ma_list = list()
    try:
        for i in obj.__dict__:
            ma_list.append(i)
    except Exception:
        return ma_list
    return ma_list
