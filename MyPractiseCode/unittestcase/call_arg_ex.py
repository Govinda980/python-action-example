import unittest
from unittest.mock import Mock


# A simple function that processes data multiple times
def process_data(func, data_list):
    for data in data_list:
        func(data)


class TestProcessData(unittest.TestCase):

    def test_call_args_list(self):
        # Create a mock function
        mock_func = Mock()

        # Call the process_data function with the mock and a list of data
        process_data(mock_func, ["data1", "data2", "data3"])

        # Check the call arguments list
        self.assertEqual(mock_func.call_count, 3)  # Verify it was called three times
        self.assertEqual(mock_func.call_args_list[0], ("data1",))  # Check the first call
        self.assertEqual(mock_func.call_args_list[1], ("data2",))  # Check the second call
        self.assertEqual(mock_func.call_args_list[2], ("data3",))  # Check the third call


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import Mock


# A simple function that processes data
def process_data(func, data):
    return func(data)


class TestProcessData(unittest.TestCase):

    def test_call_args(self):
        # Create a mock function
        mock_func = Mock()

        # Call the process_data function with the mock
        process_data(mock_func, "input data")

        # Check the last call arguments
        self.assertEqual(mock_func.call_count, 1)  # Verify it was called once
        self.assertEqual(mock_func.call_args, (("input data",), {}))  # Check the last call


if __name__ == "__main__":
    unittest.main()

