#!/usr/bin/python3

"""Define a square function"""


class Square:
    """Represent the Square function"""
    def __init__(self, size=0, position=(0, 0)):
        """initiliaze the new attrbuite
        Args:
            self (int): the int some thing
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self, value):
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            print(" " * self.__position[0], "#" * self.__size)
