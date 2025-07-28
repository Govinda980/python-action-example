import unittest


class Calculation(unittest.TestCase):

    def division_cal(self, a, b):
        c = a / b
        return c

    def test_success_division(self):
        self.assertEqual(self.division_cal(10, 2), 5)

    def test_division_error(self):
        self.assertRaises(ZeroDivisionError, self.division_cal, 10, 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)
