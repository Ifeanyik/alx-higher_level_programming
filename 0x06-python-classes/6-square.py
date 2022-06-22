#!/usr/bin/python3
'''create Square class'''


class Square:
    '''Initializing attributes'''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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
            for k in range(self.__position[1]):
                print()
            count = 0
            while count < self.__size:
                chars = 0
                for i in range(self.__position[0]):
                    print("{}".format(" "), end="")
                while chars < self.__size:
                    print("{}".format("#"), end="")
                    chars += 1
                print()
                count += 1
    '''Retrieve position'''
    @property
    def position(self):
        return self.__position
    '''Position setter'''
    @position.setter
    def position(self, value):
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
