#!/usr/bin/python3

"""Define a square class"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """initialize the init function
        Args:
            self (int): the self or head or some thing like this
        """
        self.size = size

    @property
    def size(self):
        """the property function to has an attrbute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """The setter function to set the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        """return the multiplacation size"""
        for i in range(0, self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
