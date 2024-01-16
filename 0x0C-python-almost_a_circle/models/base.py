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
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """The class method that return an instance with attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 3)
        else:
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """the class method thet return instances"""

        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding="utf-8") as f:
            damn = f.read()
            instance = cls.from_json_string(damn)
            dic = [cls.create(**value) for value in instance]
            return dic

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """The class methods that serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """return a list class instantiated from csv file"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []
