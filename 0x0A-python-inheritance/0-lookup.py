#!/usr/bin/python3
def lookup(obj):
    ma_list = list()
    for i in obj.__dict__:
        ma_list.append(i)
    return ma_list
