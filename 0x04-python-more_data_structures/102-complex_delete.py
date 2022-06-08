#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    exist = ''
    new_dict = {}
    for i in a_dictionary:
        if a_dictionary[i] == value:
            exist = True
            break
    if exist != True:
        return a_dictionary
    for i in a_dictionary:
        if a_dictionary[i] != value:
            new_dict[i] = a_dictionary[i]
    return new_dict
