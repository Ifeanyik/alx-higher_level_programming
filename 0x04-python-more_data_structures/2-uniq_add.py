#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    my_list = list(my_set)
    total = 0
    for i in my_list:
        total += i
    return total
