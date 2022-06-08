#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = [i for i in a_dictionary]
    key_list.sort()
    for i in key_list:
        print("{}: {}".format(i, a_dictionary[i]))
