import unittest
from unittest.mock import MagicMock


# A simple function that uses another function to demonstrate mocking
def process_data(func):
    for _ in range(5):
        func()


class TestProcessData(unittest.TestCase):

    def test_function_call_count(self):
        # Create a mock function
        mock_func = MagicMock()

        # Call the process_data function with the mock
        process_data(mock_func)

        # Check that the mock was called 5 times
        self.assertEqual(mock_func.call_count, 5)


if __name__ == "__main__":
    unittest.main()
