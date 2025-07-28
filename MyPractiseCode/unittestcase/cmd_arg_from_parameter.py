from parameterized import parameterized
import unittest

def add(x, y):
    return x + y

class TestAddFunction(unittest.TestCase):

    @parameterized.expand([
        ("positive_numbers", 1, 2, 3),
        ("zero", 0, 0, 0),
        ("negatives", -1, -1, -2)
    ])
    def test_add(self, name, a, b, expected):
        self.assertEqual(add(a, b), expected)

if __name__ == "__main__":
    unittest.main()
