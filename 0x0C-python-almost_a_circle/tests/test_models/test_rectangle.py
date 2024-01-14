#!/usr/bin/python3

import unittest
from rectangle import Rectangle
from base import Base


class TestRectangle(unittest.TestCase):
    """start testing a rectangle class"""

    def setUp(self):
        """Reset the objet counter befor testing"""
        pass
    Base._Base__nb_objects = 0

    def test_theFirst_Rec_base(self):
        """test all cases for the base rectangle class"""
        r1 = Rectangle(7, 8)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1,height, 8)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(7, 8, 9)
        self.assertEqual(r2.width, 7)
        self.assertEqual(r2.height, 8)
        self.assertEqual(r2.x, 9)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(2, 4, 6, 3)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 6)
        self.assertEqual(r3.y, 3)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(4, 4, 9, 9, 24)
        r4.width = 73
        r4.height = 56
        r4.x = 3
        r4.y = 1
        self.assertEqual(r4.width, 73)
        self.assertEqual(r4.height, 56)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 1)
        self.assertEqual(r4.id, 24)
        del r1, r2, r3, r4

    def test_raises(self):
        """Test wrong usage of the class"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width(self):
        """test invalid value of the width of rectangle"""
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle(7.3, "3.2")
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle("2", 3)
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle((3,), 4)
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle(None, 6)
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle(True, 6)
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle([9], 3)
        with assertRaises(TypeError, "width must be an integer"):
            Rectangle({"hay" : 9}, 3)
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle(int, 7)
        with self.assertRaises(ValueError, "width must be > 0"):
            Rectangle(-3, 2)
        with self.assertRaises(ValueError, "width must be > 0"):
            Rectangle(0, 7)
    def test_height(self):
        """test invalid value of the height of rectangle"""
        with self.assertRaises(TypeError, "height must be an integer"):
            Rectangle(4, 6.9)
        with self.assertRaises(TypeError, "height must be an integer"):
            Rectangle(4, "4")
        with self.assertRaises(TypeError, "height must be an integer"):
            o = Rectangle(5, 3)
            o.height = 4.9
        with assertRaises(TypeError, "height must be an integer"):
            Rectangle(8, (2,))
        with assertRaises(TypeError, "height must be an integer"):
            Rectangle(5, True)
        with assertRaises(TypeError, "height must be an integer"):
            Rectangle(8, [9])
        with assertRaises(TypeError, "height must be an integer"):
            Rectangle(8, None)
        with assertRaises(TypeError, "height must be an integer"):
            Rectangle(3, {"hey": 8})
        with assertRaises(TypeError, "height must be an integer"):
            Rectangle(7, int)
        with assertRaises(ValueError, "height must be > 0"):
            Rectangle(8, -5)
        with assertRaises(ValueError, "height must be > 0"):
            Rectangle(8, 0)
        with assertRaises(ValueError, "height must be > 0"):
            r = Rectangle(3, 7)
            r.height = -6
    def test_case_x(self):
        """test invalid value of the x_cordonnate of rectangle"""
        with self.assertRaises(TypeError, "x must be an integer"):
            Rectangle(4, 6, "zero")
        with self.assertRaises(TypeError, "x must be an integer"):
            Rectangle(4, 6, (5, 5))
        with self.assertRaises(TypeError, "x must be an integer"):
            Rectangle(6, 5, [6, 6])
        with self.assertRaises(TypeError, "x must be an integer"):
            Rectangle(5, 7, {"x":3})
        with self.assertRaises(TypeError, "x must be an integer"):
            Rectangle(5, 6, int)
        with self.assertRaises(TypeError, "x must be an integer"):
            Rectangle(5, 7, 3.5)
        with self.assertRaises(TypeError, "x must be >= 0"):
            Rectangle(3, 5, -3)
    def test_case_y(self):
        """test invalid value of y"""
        with self.assertRaises(TypeError, "y must be an integer"):
            Rectangle(4, 6, 5, "zero")
        with self.assertRaises(TypeError, "y must be an integer"):
            Rectangle(4, 6, 8, (5, 5))
        with self.assertRaises(TypeError, "y must be an integer"):
            Rectangle(9, 5, 7, [6, 6])
        with self.assertRaises(TypeError, "y must be an integer"):
            Rectangle(5, 7, 4, {"x":3})
        with self.assertRaises(TypeError, "y must be an integer"):
            Rectangle(5, 6, 9, int)
        with self.assertRaises(TypeError, "y must be an integer"):
            Rectangle(5, 7, 8, 3.7)
        with self.assertRaises(TypeError, "y must be >= 0"):
            Rectangle(2, 5, 9, -3)
    
    def test_area(self):
        """test the area of rectagle"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)
        r1 = Rectangle(1, 8)
        self.assertEqual(r1.area(), 8)
        r1 = Rectangle(1, 1, 1, 1, 22)
        self.assertEqual(r1.area(), 1)
