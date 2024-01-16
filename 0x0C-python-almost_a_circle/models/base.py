#!/usr/bin/python3
"""Define a base class"""
import json
import os
import csv


class Base:
    """Start a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The initialize method with id attribute"""
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method fromat to sharing data representation"""

        dic = json.dumps(list_dictionaries)
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return dic

    @classmethod
    def save_to_file(cls, list_objs):
        """the class method that writes the JSON string"""
        if list_objs is None:
            list_objs = []
        clname = cls.__name__
        filename = f"{clname}.json"
        json_string = cls.to_json_string(list_objs)
        with open(filename, 'w') as f:
            f.write(json_string)
