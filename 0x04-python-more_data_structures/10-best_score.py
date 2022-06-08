#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    big_key = 0
    for i in a_dictionary:
        if a_dictionary[i] > big_key:
            big_key = a_dictionary[i]
    for i in a_dictionary:
        if a_dictionary[i] == big_key:
            big_key = i
    return big_key
