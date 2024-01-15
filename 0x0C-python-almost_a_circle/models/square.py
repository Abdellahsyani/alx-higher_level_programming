#!/usr/bin/python3
"""Define a Square class"""
from  import rectangle



class Square(rectangle.Rectangle):
    """Start a square class that inhert from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """define an initializes for new square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size methods"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size square"""
        self.width = value
        self.height = value

    def __str__(self):
        """the __str__ methods"""
        seq = "[Square] " + "(" + self.id + ") " + self.x
        seq += "/ " + self.y + " - " + self.width
        return seq

s1 = Square(5)
print(s1)
print(s1.area())
s1.display()

print("---")

s2 = Square(2, 2)
print(s2)
print(s2.area())
s2.display()

print("---")

s3 = Square(3, 1, 3)
print(s3)
print(s3.area())
s3.display()
