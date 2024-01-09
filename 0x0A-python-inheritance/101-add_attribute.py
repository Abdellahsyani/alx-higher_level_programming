#!/usr/bin/python3
"""Module to manipulate attributes of objects."""


def add_attribute(obj, attr, value):
    """Add or modify obj's attr with value."""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
