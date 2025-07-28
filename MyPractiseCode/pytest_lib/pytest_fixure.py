import pytest


def add(a, b):
    return a + b


"""
 Why use @pytest_lib.fixture?
✔ Reusable setup without setUp().
✔ More flexible than unittest.
"""


@pytest.fixture
def sample_data():
    return {"a": 10, "b": 5}


def test_add(sample_data):
    assert add(sample_data["a"], sample_data["b"]) == 15


@pytest.fixture
def input_value():
    input = 39
    return input


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

@pytest.mark.skip
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0


@pytest.fixture
def get_item():
    return ["apple", "orange", "banana"]


def test_check_len(get_item):
    assert len(get_item) == 3


@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 3, 5)
])
def test_multiple_input(a, b, result):
    assert a + b == result

@pytest.mark.xfail
def test_greater():
    num = 100
    assert num > 100

# pytest test_failure.py -v ---->maxfail 1  stop if one test fail
