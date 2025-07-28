# import random
# print(random.random())  # give float in range 0 to 1
# print(random.uniform(1, 100))  # any one float in range 1 to 100
# print(random.randint(1, 100))  # any one integer from 1 to 100
# print(random.randrange(0, 100, 2))  # any one 1 to 100 even num
# print(random.sample(range(1, 100), 3))  # return 3 random number
# print(list(range(1, 5)))

import unittest


class Calculation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1 + 2, 3)

    def test_sub(self):
        self.assertEqual(2 - 1, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
