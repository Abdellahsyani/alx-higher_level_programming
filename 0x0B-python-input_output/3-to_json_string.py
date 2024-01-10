#!/usr/bin/python3
"""Module to convert Python objects to string of JSON."""
import json


def to_json_string(my_obj):
    """Get the JSON representaion of an object as a string."""
    return json.dumps(my_obj)
