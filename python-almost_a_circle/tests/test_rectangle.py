#!/usr/bin/python3
"""unittest for Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle class tests"""

    def test_rectangle_area(self):
        """Area test"""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_to_dictionary(self):
        """dictionary test"""
        r = Rectangle(4, 5, 1, 2, 42)
        r_dict = r.to_dictionary()
        expected_dict = {'id': 42, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertDictEqual(r_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
