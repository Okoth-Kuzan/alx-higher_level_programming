import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_creation(self):
        square1 = Square(5)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square1.width, 5)
        self.assertEqual(square1.height, 5)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)
        self.assertIsNone(square1.id)

        square2 = Square(3, 2, 1, 42)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.width, 3)
        self.assertEqual(square2.height, 3)
        self.assertEqual(square2.x, 2)
        self.assertEqual(square2.y, 1)
        self.assertEqual(square2.id, 42)

    def test_size_property(self):
        square = Square(4)
        self.assertEqual(square.size, 4)

        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

        with self.assertRaises(ValueError):
            square.size = -3

    def test_to_dictionary(self):
        square = Square(2, 1, 3, 5)
        square_dict = square.to_dictionary()

        expected_dict = {
            "id": 5,
            "size": 2,
            "x": 1,
            "y": 3,
        }

        self.assertEqual(square_dict, expected_dict)

    def test_update_method(self):
        square = Square(3, 2, 1, 10)

        square.update(5, 6, 7, 8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

        square.update(id=15, x=3)
        self.assertEqual(square.id, 15)
        self.assertEqual(square.x, 3)

    def test_str_representation(self):
        square = Square(4, 2, 1, 5)
        expected_str = "[Square] (5) 2/1 - 4"
        self.assertEqual(str(square), expected_str)


if __name__ == "__main__":
    unittest.main()

