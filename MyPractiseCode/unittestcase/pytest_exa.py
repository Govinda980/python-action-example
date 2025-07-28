import pytest


def add(x, y):
    return x + y


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert (10 - 5) != 3
