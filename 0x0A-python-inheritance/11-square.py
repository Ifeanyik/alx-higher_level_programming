#!/usr/bin/python3
'''Implement square object'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defines square object attributes'''
    def __init__(self, size):
        '''Initialise object attributes'''
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Calculate Square object area'''
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
