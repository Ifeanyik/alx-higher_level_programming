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
