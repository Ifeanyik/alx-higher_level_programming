#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if str.index(i) == len(str) - 1:
            emi = "\n"
        else:
            emi = ""
        if ord(i) in range(97, 123):
            print("{}".format(chr(ord(i) - 32)), end=emi)
        else:
            print("{}".format(i), end="")
