#!/usr/bin/python3
def no_c(my_string):
    if my_string == "":
        return ""
    new = list(my_string[:])
    o_new = str()
    for i in new:
        if i == "c" or i == "C":
            new.pop(new.index(i))
    for i in new:
        o_new += i
    return o_new
