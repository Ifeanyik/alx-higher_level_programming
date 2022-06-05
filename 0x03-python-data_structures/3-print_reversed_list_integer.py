#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_list.sort(reverse=True)
    for i in my_list:
        print("{:d}".format(i))
