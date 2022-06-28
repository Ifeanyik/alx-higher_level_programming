#!/usr/bin/python3
'''Implement LockedClass Object'''


class LockedClass:
    def __setattr__(self, __name, __value):
        '''Stops any attribute other than first_name from being set'''
        if __name != "first_name":
            run = "'LockedClass' object has no attribute '{}'".format(__name)
            raise AttributeError(run)
        self.__dict__[__name] = __value
