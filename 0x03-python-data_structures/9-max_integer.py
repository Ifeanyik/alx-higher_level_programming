#!/usr/bin/python3
def max_integer(my_list=[]):
    iter_num = len(my_list)
    if iter_num == 0:
        return None
    current_element = my_list[0]
    for i in range(iter_num):
        if current_element < my_list[i]:
            current_element = my_list[i]
    return current_element
