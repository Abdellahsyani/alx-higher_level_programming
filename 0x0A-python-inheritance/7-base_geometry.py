#!/usr/bin/python3
"""Module to make and manipulate geometry."""


class BaseGeometry:
    """The base class of the geometry."""

    def area(self):
        """Calcutale the area of the geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that `value` is an int."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
