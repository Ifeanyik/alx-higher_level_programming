#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l_copy = my_list[:]
    if idx < 0:
        return l_copy
    if idx >= len(my_list):
        return l_copy
    l_copy[idx] = element
