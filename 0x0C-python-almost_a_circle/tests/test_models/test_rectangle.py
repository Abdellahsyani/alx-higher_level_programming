#!/usr/bin/python3
"""Unit testing for the rectangle Module"""
import unittest
import doctest
from models.rectangle import Rectangle
from models.base import Base



class TestRectangle(unittest.TestCase):
    """start testing a rectangle class"""

    def setUp(self):
        """Reset the objet counter befor testing"""
        Base._Base__nb_objects = 0

    def test_theFirst_Rec_base(self):
        """test all cases for the base rectangle class"""
        r1 = Rectangle(7, 8)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 8)
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
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(7.3, "3.2")
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("2", 3)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle((3,), 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(None, 6)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(float, 6)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle([9], 3)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle({"hay" : 9}, 3)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(int, 7)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-3, 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 7)

    def test_height(self):
        """test invalid value of the height of rectangle"""
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(4, 6.9)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(4, "4")
        with self.assertRaises(TypeError, msg="height must be an integer"):
            o = Rectangle(5, 3)
            o.height = 4.9
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(8, (2.6,))
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, "True")
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(8, [9])
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(8, None)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(3, {"hey": 8})
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(7, int)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(8, -5)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(8, 0)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r = Rectangle(3, 7)
            r.height = -6

    def test_case_x(self):
        """test invalid value of the x_cordonnate of rectangle"""
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(4, 6, "zero")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(4, 6, (5, 5))
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(6, 5, [6, 6])
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(5, 7, {"x":3})
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(5, 6, int)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(5, 7, 3.5)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(3, 5, -3)

    def test_case_y(self):
        """test invalid value of y"""
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(4, 6, 5, "zero")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(4, 6, 8, (5, 5))
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(9, 5, 7, [6, 6])
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(5, 7, 4, {"x":3})
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(5, 6, 9, int)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(5, 7, 8, 3.7)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(2, 5, 9, -3)
    
    def test_area(self):
        """test the area of rectagle"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)
        r1 = Rectangle(1, 8)
        self.assertEqual(r1.area(), 8)
        r1 = Rectangle(1, 1, 1, 1, 22)
        self.assertEqual(r1.area(), 1)

    def test_display(self):
        """test the display methods:

        >>> r = Rectangle(4, 5)
        >>> r.display()
        ####
        ####
        ####
        ####
        ####
        >>> r.height = 3
        >>> r.display()
        ####
        ####
        ####
        >>> del r
        >>> r = Rectangle(3, 3, 2, 2)
        >>> r.display()
        <BLANKLINE>
        <BLANKLINE>
          ###
          ###
          ###
        >>> del r
        >>> r = Rectangle(3, 2, 3)
        >>> r.display()
           ###
           ###
        >>> del r
        >>> r = Rectangle(3, 2, 0, 3)
        >>> r.display()
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        ###
        ###
        >>> del r
        """
        finder = doctest.DocTestFinder()
        suite = doctest.DocTestSuite(test_finder = finder)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def test__str__methods(self):
        """test __str__ representation of class"""
        r1 = Rectangle(8, 6, 4, 3, 13)
        self.assertEqual(str(r1), "[Rectangle] (13) 4/3 - 8/6")
        r1.height = 9
        self.assertEqual(str(r1), "[Rectangle] (13) 4/3 - 8/9")
        r2 = Rectangle(5, 7, 9)
        self.assertEqual(str(r2), "[Rectangle] (1) 9/0 - 5/7")
        r2.y = r2.x
        self.assertEqual(str(r2), "[Rectangle] (1) 9/9 - 5/7")
        r3 = Rectangle(3, 9)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 3/9")
        r4 = Rectangle(7, 7, 7, 7, 7)
        self.assertEqual(str(r4), "[Rectangle] (7) 7/7 - 7/7")
        del r1, r2, r3, r4

    def test_update(self):
        """test the first update method in class attributes"""
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")
        r.update()
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")
        r.update(11)
        self.assertEqual(str(r), "[Rectangle] (11) 10/10 - 10/10")
        r.update(11, 12)
        self.assertEqual(str(r), "[Rectangle] (11) 10/10 - 12/10")
        r.update(11, 12, 13)
        self.assertEqual(str(r), "[Rectangle] (11) 10/10 - 12/13")
        r.update(11, 12, 13, 14)
        self.assertEqual(str(r), "[Rectangle] (11) 14/10 - 12/13")
        r.update(11, 12, 13, 14, 15)
        self.assertEqual(str(r), "[Rectangle] (11) 14/15 - 12/13")
        r.update(11, 2, 3, 4, 5, 6, 7, 8, "cool", {"habite": 99})
        self.assertEqual(str(r), "[Rectangle] (11) 4/5 - 2/3")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(11, 12, 13, (14, 5))
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(11, [12, 13])
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(11, -12, [12, 13])
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(11, 0, [12, 13])
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r.update(11, 12, 13, 14, -15)
        del r

    def test_update2(self):
        """second update test """
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(x=1, height=2, y=3, id=98)
        self.assertEqual(str(r), "[Rectangle] (98) 1/3 - 1/2")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (98) 1/3 - 4/2")
        r.update(cords=(33, 12), area=2, betty="best", x=2, dimontial=[23, 80])
        self.assertEqual(str(r), "[Rectangle] (98) 2/3 - 4/2")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(x=1.3, height=2, y=3, width=4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(x=1, height=(2,), y=3, width="4")
        with self.assertRaises(TypeError, msg="heigth must be an integer"):
            r.update(x=1, height=(2,), y=3, width=4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(width = [2, 3, 5])
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(width = -2, height = 0)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r.update(width=2, height=0)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r.update(width = 2, x = -3)
        del r
