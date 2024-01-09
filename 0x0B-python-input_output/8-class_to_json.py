#!/usr/bin/python3
"""make a dictionary form the attributes of any object."""


def class_to_json(obj):
    """Get a dictionary of simple data structures related to an object."""
    json_dict = {}
    obj_dict = obj.__dict__
    simple_types = [list, dict, str, int, float, bool]
    for k, v in obj_dict.items():
        if type(v) in simple_types:
            json_dict[k] = v
    else:
        return json_dict
