import pytest


def add(a, b):
    return a + b


def divide(a, b):

    res = a / b
    return res


def test_add():
    x = 2
    y = 3
    assert add(x, y) == 5


def test_add_to_negative():
    x = -1
    y = -3
    assert add(x, y) == -4


def test_divide_exception():
    x = 4
    y = 0
    pytest.raises(ZeroDivisionError, divide, x, y)
