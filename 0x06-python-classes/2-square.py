#!/usr/bin/python3

"""Define a classe square"""


class Square:
    '''request a square'''

    def __init__(self, size=0):
        '''initialize a square'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''return square'''
        return (self.__size * self.__size)
