#!/usr/bin/python3
"""Define a Rectangle class"""
from base import Base


class Rectangle(Base):
    """starting the Rectangle class with Base inherts"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """define an initializes methods"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get and setter class"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get and setter class"""
        return self.__height

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get and setter class"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get and setter class"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the square area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the square area with # character"""
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """return the str"""
        rect = "[Rectangle] " + "(" + str(self.id) + ") " + str(self.x)
        rect += "/" + str(self.y) + " - " + str(self.width) + "/" + str(self.height)
        return rect

r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)

r2 = Rectangle(5, 5, 1)
print(r2)
