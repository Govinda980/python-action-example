import unittest
import sys

class TestMathOperations(unittest.TestCase):
    # @unittest.skipUnless(sys.platform == "linux", "Skipping test unless on Linux")
    @unittest.skipIf(sys.platform == "win32", "Skipping test on Windows")
    def test_addition(self):
        result = 1 + 1
        self.assertEqual(result, 2)

    @unittest.skipIf(sys.version_info < (3, 7), "Skipping test on Python versions < 3.7")
    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
