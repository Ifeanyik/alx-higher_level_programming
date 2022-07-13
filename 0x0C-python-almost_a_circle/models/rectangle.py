#!/usr/bin/python3
'''Implement base class'''


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    '''Implement Rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Retrieve value of width'''
        return self.__width

    @width.setter
    def width(self, width):
        '''Sets value of width'''
        if isinstance(width, int):
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        '''Retrieve height value'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Sets height value'''
        if isinstance(height, int):
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        '''Retrieves value of x'''
        return self.__x

    @x.setter
    def x(self, x):
        '''Sets value of x'''
        if isinstance(x, int):
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        '''Retireves value of y'''
        return self.__y

    @y.setter
    def y(self, y):
        '''Sets value of y'''
        if isinstance(y, int):
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
        else:
            raise TypeError("y must be an integer")

    def area(self):
        '''Returns area of Rectangle instance'''
        return self.__height * self.__width

    def display(self):
        '''Prints out Rectangle instance'''
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x, end="")
            for column in range(self.__width):
                print("#", end="")
            print()
            if row == self.__height - 1:
                break

    def __str__(self):
        '''Return string representation of object'''
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height
        str_repr = "[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e)
        return str_repr

    def update(self, *args, **kwargs):
        '''Assigns arguments to attributes'''
        if args:
            arg_list = []
            for i in args:
                arg_list.append(i)
            try:
                self.id = arg_list[0]
                self.width = arg_list[1]
                self.height = arg_list[2]
                self.x = arg_list[3]
                self.y = arg_list[4]
            except IndexError:
                pass
        else:
            for i in kwargs:
                if i == "height":
                    self.height = kwargs["height"]
                elif i == "width":
                    self.width = kwargs["width"]
                elif i == "x":
                    self.x = kwargs["x"]
                elif i == "y":
                    self.y = kwargs["y"]
                else:
                    self.id = kwargs["id"]

    def to_dictionary(self):
        '''returns dict representation of instance'''
        a = self.id
        b = self.width
        c = self.height
        d = self.x
        e = self.y
        dict_repr = {"id": a, "width": b, "height": c, "x": d, "y": e}
        return dict_repr
