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
        if type(value) != int:
            raise TypeError("size must be an integer")
        self.__size = value
    '''Prints the square with # character'''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            count = 0
            while count < self.__size:
                chars = 0
                while chars < self.__size:
                    print("{}".format("#"), end="")
                    chars += 1
                print()
                count += 1
