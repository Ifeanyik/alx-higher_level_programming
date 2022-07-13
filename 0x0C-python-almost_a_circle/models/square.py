#!/usr/bin/python3
'''Module that defines square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''Returns string representation of object'''
        a = self.id
        x = self.x
        y = self.y
        c = self.size
        str_repr = "[Square] ({}) {}/{} - {}".format(a, x, y, c)
        return str_repr

    @property
    def size(self):
        '''Retrieve size value'''
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__size = value
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        '''Update instance attributes'''
        if args:
            try:
                lame = [*args]
                self.id = lame[0]
                self.size = lame[1]
                self.x = lame[2]
                self.y = lame[3]
            except IndexError:
                pass
        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                elif i == "size":
                    self.size = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]

    def to_dictionary(self):
        '''returns dict representation of instance'''
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
