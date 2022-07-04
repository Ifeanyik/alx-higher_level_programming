#!/usr/bin/python3
'''Create class'''


class BaseGeometry:
    '''Defining class attributes'''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates a string value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''defining class attributes'''
    def __init__(self, width, height):
        '''Initialiser'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
