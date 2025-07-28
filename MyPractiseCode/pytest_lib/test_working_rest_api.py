import pytest
import requests
from unittest import mock


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError


@mock.patch("requests.get")
def test_get_user(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Eric Yang"}
    mock_get.return_value = mock_response
    data = get_users()
    assert data == {"id": 1, "name": "Eric Yang"}


@mock.patch("requests.get")
def test_get_user_httperror(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        get_users()
