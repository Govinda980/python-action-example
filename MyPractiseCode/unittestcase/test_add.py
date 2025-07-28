import unittest


class testAdd(unittest.TestCase):

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_check_addition(self):
        self.assertEqual(1 + 2, 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
