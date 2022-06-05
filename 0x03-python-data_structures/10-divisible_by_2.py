#!/usr/bin/python3
def divisible_by_2(do=[]):
    l_length = len(do)
    new_list = []
    if l_length == 0:
        return None
    for i in range(l_length):
        if do[i] % 2:
            new_list.append(False)
        else:
            new_list.append(True)
    return new_list
