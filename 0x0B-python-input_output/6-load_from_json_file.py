#!/usr/bin/python3
"""Module to get Python objects from JSON files."""
import json


def load_from_json_file(filename):
    """Get the JSON representaion of an object from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)
