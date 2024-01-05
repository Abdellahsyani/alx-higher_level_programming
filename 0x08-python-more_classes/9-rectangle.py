#!/usr/bin/python3
'''Define a rectangle class'''


class Rectangle:
    '''start a rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''The init methods '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        '''get and set of rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''return the area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Return the perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''print rectangle with #'''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''The repr methods'''
        rect = "Rectangle(" + str(self.__height)
        rect += ", " + str(self.__width) + ")"
        return (rect)

    def __del__(self):
        '''return message if the rectangle delete'''
        numbre_of_instances -= 1
        print("Bye rectangle...")
