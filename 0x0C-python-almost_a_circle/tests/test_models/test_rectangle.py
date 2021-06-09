#!/usr/bin/python3
""" Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleValues(unittest.TestCase):
    """ Testing class
        test different cases Base class values
    """

    def test_rectangle(self):
        """ Test Rectangle - Basic intranet cases
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)
        r5 = Rectangle(2, 10)
        self.assertEqual(r5.area(), 20)
        r6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r6.area(), 56)


if __name__ == '__main__':
    unittest.main()
