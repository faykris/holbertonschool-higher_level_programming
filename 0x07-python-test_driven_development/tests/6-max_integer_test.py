#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestIntValues(unittest.TestCase):
    """ Testing class
        test different cases to the max_integer function
    """
    def test_int(self):
        """ test_int method
            evaluate the result of different values
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([2, 1, 1, 1, 2]), 2)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("string"), "t")
        self.assertEqual(max_integer(["a", "l", "z"]), "z")
        self.assertEqual(max_integer(["Z", "L", "a"]), "a")
        self.assertEqual(max_integer((1, 3, 2, 4)), 4)
        self.assertEqual(max_integer([0, 0.1, 0.05, 0.1005]), 0.1005)


if __name__ == '__main__':
    unittest.main()
