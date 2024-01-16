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

    def to_json_string(list_dictionaries):
        """method fromat to sharing data representation"""
        dic = json.dumps(list_dictionaries)
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return dic
