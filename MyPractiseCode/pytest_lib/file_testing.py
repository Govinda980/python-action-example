import pytest


@pytest.fixture
def open_file():
    file = open("test.txt", "w")
    yield file
    file.close()  # Teardown after test


# Separates setup and teardown code

def test_file_write(open_file):
    open_file.write("Hello, World!")


@pytest.mark.repeat(3)
def test_run_multiple_times():
    assert True
