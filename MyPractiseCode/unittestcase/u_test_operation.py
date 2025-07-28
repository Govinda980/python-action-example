import unittest
from unittest.mock import patch, Mock

# python -m unittest unittestcase.simple_test.Arithmetic
# python -m unittest unittestcase.simple_test.Arithmetic.test_sum_vali
from unittestcase.operation import opera


class Arithmetic(unittest.TestCase):

    def setUp(self):
        self.OP = opera(10, 5)

    def test_sum_vali(self):
        self.assertEqual(1 + 2, 3)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_string_methods(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertRaises(ValueError, int, 'a')
        self.assertAlmostEqual(1.000000002, 1.000000003)
        # self.assertAlmostEqual(result, 0.3, places=7)

    def test_div_num_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.OP.div_num(10, 0)

    @unittest.skip("Skipping test_div_num")
    def test_div_num(self):
        self.assertEqual(self.OP.div_num(10, 2), 5)

    @patch('unittestcase.operation.opera.div_num')
    def test_call_div_num(self, mock_div):
        mock_div.return_value = Mock()
        self.OP.call_div_num()


if __name__ == '__main__':
    unittest.main(verbosity=2)

    #unittest.main(verbosity=2): This line sets the verbosity level to 2, which means you will see detailed information
    # about each test being run, including the name of the test and whether it passed or failed
