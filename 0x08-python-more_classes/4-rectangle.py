#!/usr/bin/python3
'''Create Rectangle class'''


class Rectangle:
    '''Defining class attributes'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Retrieve width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets width value and ensures width is an integer'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrieve height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets height and ensures it is an integer not less than 0'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns value of rectangle area'''
        self.height = self.__height
        self.width = self.__width
        return self.height * self.width

    def perimeter(self):
        '''Returns perimeter of rectangle object'''
        if self.__height == 0 or self.__width == 0:
            return 0
        self.height = self.__height
        self.width = self.__width
        return 2 * (self.height + self.width)

    def __str__(self):
        '''Runs when print() or str() is used on a Rectangle objects'''
        self.height = self.__height
        self.width = self.__width
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
        return str()

    def __repr__(self):
        '''Runs when repr() is called'''
        return f"Rectangle"
