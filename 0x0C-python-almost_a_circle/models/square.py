#!/usr/bin/python3
"""Define a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """get args and kwargs from these"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)
