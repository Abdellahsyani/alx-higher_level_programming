#!/usr/bin/python3


class Square:
    """request the class"""
    def __init__(self, size=0):
        """the unit funtion
        @sefl.__size: the size of class
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """The property function
        return the size
    """
        return sefl.__size

    @size.setter
    def size(self, value):
        """the setter function to set value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """the area function to be attrbute"""
        return self.__size
