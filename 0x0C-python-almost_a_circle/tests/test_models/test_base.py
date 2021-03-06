#!/usr/bin/python3
""" Unittest for Base
"""
import unittest
from models.base import Base


class TestBaseValues(unittest.TestCase):
    """ Testing class
        test different cases Base class values
    """

    def test_base(self):
        """ Test base - Basic intranet cases
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        """ Other test cases """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertTrue(Base.from_json_string('[{ "id": 89 }]'), True)
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{ "id": 89 }])

if __name__ == '__main__':
    unittest.main()
