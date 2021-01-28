#!/usr/bin/python3
import json

'''Defines Class Base, the class will be the parent
of the Rectangle and Square class'''


class Base:
    '''Parent class to avoid redundancy with common methods
    and determinate the id of each item'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize the class with the 'id' if it is pased
        otherwhise set the 'id' automatycally to avoid redundancy
        in the child class'''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return the JSON string representation of list_dictionaries
        if the imput is empty return a empty string'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_obj):
        '''Saves a JSON string representation into a file with the name of
        the file followed with '.json' extencion'''
        f_name = cls.__name__ + '.json'
        f_data = []
        if list_obj is not None:
            for i in list_obj:
                f_data += [i.to_dictionary()]
        with open(f_name, 'w', encoding='utf-8') as fd:
            fd.write(cls.to_json_string(f_data))

    @staticmethod
    def from_json_string(json_string):
        '''Read a string and return a dictionare with all the
        object data'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set
        with the dictionary data'''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(1,1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Return a list with the instances in a file, if the file is
        empty or do not exist the list will be empty'''
        fn = cls.__name__ + '.json'
        ls = []
        tmp = []
        with open(fn, 'r', encoding='utf-8') as fd:
            tmp += cls.from_json_string(fd.read())
        for i in tmp:
            ls += [str(cls.create(**i))]
        return ls
