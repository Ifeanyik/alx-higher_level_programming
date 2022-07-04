#!/usr/bin/python3
def lookup(obj):
    '''Returns list of object attributes'''
    ma_list = list()
    for i in obj.__dict__:
        ma_list.append(i)
    return ma_list
