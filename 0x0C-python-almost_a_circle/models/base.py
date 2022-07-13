#!/usr/bin/python3
'''Contains base class'''

import json


class Base:
    '''Implement Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Implement class constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns JSON representation of parameters'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        json_list = []
        for i in list_dictionaries:
            try:
                json_list.append(i.to_dictionary())
            except AttributeError:
                if type(i) == dict:
                    json_list.append(i)
        json_string = json.dumps(json_list)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes JSON string to a file'''
        file_name = "{}.json".format(cls.__name__)
        if list_objs is None or list_objs == []:
            json_list = cls.to_json_string([])
        else:
            a = list_objs[0]
            json_list = cls.to_json_string(list_objs)
        with open(file_name, "w") as myFile:
            myFile.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        '''Returns list of JSON string representation'''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns instance with set attributes'''
        if cls.__name__ == "Rectangle":
            dummy_instance = Rectangle(4, 4)
        elif cls.__name__ == "Square":
            dummy_instance = Square(2)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''Returns list of instances'''
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as myFile:
                file_cont = myFile.read()
                dict_list = json.loads(file_cont)
                instance_list = []
                for i in dict_list:
                    if cls.__name__ == "Rectangle":
                        instance = Rectangle.create(**i)
                        instance_list.append(instance)
                    elif cls.__name__ == "Square":
                        instance = Square.create(**i)
                        instance_list.append(instance)
                return instance_list
        except FileNotFoundError:
            return []
