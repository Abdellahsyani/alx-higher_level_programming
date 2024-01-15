#!/usr/bin/python3
"""testing the square class"""
import unittest
import doctest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """test the base class"""

    def setUp(self):
        """set up number to zero befor starting"""
        Base._Base__nb_objects = 0

    def test_square(self):
        """testing normal usage"""
        sq = Square(5)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.area(), 25)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 5")
        sq.size = 4
        self.assertEqual(sq.size, 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            sq.size = "an"

    def test_raises(self):
        """test wrong usage"""
        with self.assertRaises(TypeError):
            Square()
