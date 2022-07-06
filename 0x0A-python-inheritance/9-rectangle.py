#!/usr/bin/python3
'''Create class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''defining class attributes'''
    def __init__(self, width, height):
        '''Initialiser'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''computes area of object'''
        return self.__width * self.__height

    def __str__(self):
        '''Called when str is called on an obj'''
        f = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return f
