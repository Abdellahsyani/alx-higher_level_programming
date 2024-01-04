#!/usr/bin/python3
'''Define a rectangle class'''


class Rectangle:
    '''The Rectangle class defined'''

    def __init__(self, width=0, height=0):
        '''initialize a new Rectangle
        Args:
            width(int): The width of rectangle
            height(int): the height of new rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get and set the width of rectangle'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Get and set the height of rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return the area of reactangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Return the perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Return the printable representation with character #'''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
