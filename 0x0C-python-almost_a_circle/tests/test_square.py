#!/usr/bin/python3
"""Unittests for Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_size(self):
        """Test size getter and setter"""
        square = Square(5)
        self.assertEqual(square.size, 5)

        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_str(self):
        """Test __str__ method"""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update(self):
        """Test update method"""
        square = Square(3, 1, 1, 1)
        square.update(10)
        self.assertEqual(str(square), "[Square] (10) 1/1 - 3")

        square.update(11, 5, 5, 5)
        self.assertEqual(str(square), "[Square] (11) 5/5 - 5")

        square.update(size=7, id=2, x=0, y=0)
        self.assertEqual(str(square), "[Square] (2) 0/0 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()

        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()

