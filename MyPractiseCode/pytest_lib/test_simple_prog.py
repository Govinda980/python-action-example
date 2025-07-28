import math
import pytest


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_square():
    num = 7
    assert 7 * 7 == 40


def test_equality():
    assert 10 == 11


@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
