#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, __name, __value):
        if __name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(__name))
        self.__dict__[__name] = __value
