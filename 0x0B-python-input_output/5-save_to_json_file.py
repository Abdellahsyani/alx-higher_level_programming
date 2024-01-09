#!/usr/bin/python3
"""Module to save Python objects into JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """Get the JSON representaion of an object as a string."""
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
