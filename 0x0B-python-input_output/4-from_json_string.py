#!/usr/bin/python3
"""Module to convert a string of JSON to Python objects."""
import json


def from_json_string(my_str):
    """Get the object from JSON representaion string."""
    return json.loads(my_str)
