#!/usr/bin/python3
'''Defines class Student'''


class Student:
    '''Defining Student object attributes'''
    def __init__(self, first_name, last_name, age):
        '''Initialising object attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieve dict representation of obj attributes'''
        res = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    if hasattr(self, i):
                        res[i] = self.__dict__[i]
            return res
        return self.__dict__.copy()

    def reload_from_json(self, json):
        '''Replaces all attributes of obj dict'''
        for attr in json:
            self.__dict__[attr] = json[attr]
