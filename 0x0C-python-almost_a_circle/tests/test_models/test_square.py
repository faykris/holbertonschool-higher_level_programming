#!/usr/bin/python3
""" Unittest for Square
"""
import unittest
from models.square import Square


class TestRectangleValues(unittest.TestCase):
    """ Testing class
        test different cases Base class values
    """

    def test_rectangle(self):
        """ Test Rectangle - Basic intranet cases
        """
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        s2 = Square(2)
        self.assertEqual(s2.id, 2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.id, 12)

        s4 = Square(3)
        self.assertEqual(s4.area(), 9)
        s5 = Square(2, 0, 0)
        self.assertEqual(s5.area(), 4)
        s6 = Square(8, 0, 0, 12)
        self.assertEqual(s6.area(), 64)


if __name__ == '__main__':
    unittest.main()
