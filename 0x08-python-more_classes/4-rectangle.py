#!/usr/bin/python3
'''Define a rectangle class'''


class Rectangle:
    '''Start a rectangle class'''
    def __init__(self, width=0, height=0):
        '''define another rectangle
        Args:
            width(int): the width of rectangle
            height(int): the height of rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get and set of rectangle'''
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
        '''Get and set of rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''return premiter rectangle'''
        if self.width == 0 or self.height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Return the representation of rectangle'''
        if self.width == 0 or self.height == 0:
            return ("")
        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        '''Return the representation of recangle'''
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle
