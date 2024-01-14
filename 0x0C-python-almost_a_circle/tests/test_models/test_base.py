#!/usr/bin/python3
"""Start unittest for base module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test the base class"""
    
    def setUp(self):
        """set a setUp methods to set aleach number at zero"""
        Base._Base__nb_objects = 0

    def test_cases(self):
        """start testing cases"""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
        del obj1, obj2, obj3

if __name__ == "__main__":
    unittest.main()
