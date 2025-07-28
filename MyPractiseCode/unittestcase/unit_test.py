import unittest


def square(n):
    return n * n


def cube(n):
    return n * n * n


class TestCase(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_cube(self, mock_c):
        # self.assertEqual(cube(2), 8)
        self.cube(2).return_value = 8
