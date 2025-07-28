import unittest
import sys

def multiply(x, y):
    return x * y

class TestMath(unittest.TestCase):
    def test_multiply(self):
        x = int(sys.argv[1]) if len(sys.argv) > 1 else 2
        y = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        expected = x * y
        self.assertEqual(multiply(x, y), expected)

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
