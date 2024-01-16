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
        clname = cls.__name__
        filename = f"{clname}.json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dic = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(dic))
    
    @staticmethod
    def from_json_string(json_string):
        """the static method that returns the list of JSON string"""
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)
