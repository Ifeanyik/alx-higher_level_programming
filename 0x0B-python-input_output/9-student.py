#!/usr/bin/python3
'''Module defines Student class'''


class Student:
    '''Defining Student object attributes'''
    def __init__(self, first_name, last_name, age):
        '''Initialising object attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Retrieve dict representation of obj attributes'''
        return self.__dict__.copy()
