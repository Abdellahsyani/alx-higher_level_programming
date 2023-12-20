#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """represent a class square"""

    def __init__(self, size=0):
        """initialize a new square area
        Args:
        @sefl.__size: the size of class
        """
        self.size = size

    @property
    def size(self):
        """The property function"""
        return (sefl.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """the area function to be attrbute"""
        return (self.__size * self.__size)
