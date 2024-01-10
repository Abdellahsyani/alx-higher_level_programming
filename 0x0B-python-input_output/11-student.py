#!/usr/bin/python3
"""Convert a student to JSON."""


class Student():
    """Define a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        self_dict = {}
        accepted_keys = attrs or self.__dict__
        accepted_types = [list, dict, str, int, float, bool]
        for k, v in self.__dict__.items():
            if type(v) in accepted_types and k in accepted_keys:
                self_dict[k] = v
        return self_dict

    def reload_from_json(self, json):
        """Replace student attributes with the ones in json."""
        self.__dict__.update(json)
