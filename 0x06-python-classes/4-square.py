#!/usr/bin/python3
'''create Square class'''


class Square:
    '''Initializing attributes'''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    '''Returns area of square'''
    def area(self):
        return self.__size * self.__size

    '''Retrieve size attribute'''
    @property
    def size(self):
        return self.__size

    '''Set size attribute'''
    @size.setter
    def size(self, value):
        self.__size = value
