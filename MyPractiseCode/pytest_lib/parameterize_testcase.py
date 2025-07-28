import pytest

@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30),
])
def test_addition(a, b, result):
    assert a + b == result


@pytest.mark.parametrize("input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(input, expected):
    assert eval(input) == expected
