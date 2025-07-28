import unittest
from unittest.mock import Mock


# Code to be tested
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    try:
        result = x / y
        return result
    except Exception as e:
        print(e)


def character_count(name):
    uniq_character = []
    ch_count = {}
    for ch in name:
        if ch not in uniq_character:
            uniq_character.append(ch)
    for c in uniq_character:
        ch_count[c] = name.count(c)
    return ch_count


def range_num(n):
    for i in range(n):
        print(i)


class Calculator(unittest.TestCase):

    def setUp(self):
        self.a = 20
        self.b = 10

    def test_add(self):
        self.assertEqual(add(self.a, self.b), 30)

    def test_subtract(self):
        self.assertEqual(subtract(self.a, self.b), 10)

    def test_divide(self):
        self.assertAlmostEqual(divide(self.a, self.b), 2)

    def test_divide_exception(self):
        a = 10
        b = 0
        self.assertRaises(Exception, divide(a, b))

    def test_character_count(self):
        name = "Riyansh"
        self.assertEqual(character_count(name), {'R': 1, 'i': 1, 'y': 1, 'a': 1, 'n': 1, 's': 1, 'h': 1})


if __name__ == '__main__':
    unittest.main(verbosity=2)
