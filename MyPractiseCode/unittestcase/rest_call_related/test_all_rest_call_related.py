import unittest
from unittest.mock import patch, Mock
from restcall.all_rest_call_related import RestOperation  # Update path if needed
import requests


class TestRestOperation(unittest.TestCase):

    def setUp(self):
        """Initialize the RestOperation instance before each test."""
        self.api = RestOperation()

    ### ✅ GET REQUEST TESTS ###
    @patch("requests.get")
    def test_get_post_success(self, mock_get):
        """Test GET request success case."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.ok = True
        mock_response.json.return_value = [{'userId': 1, 'id': 1, 'title': 'Test', 'body': 'Body'}]
        mock_get.return_value = mock_response

        self.api.get_post()
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_get_post_failure(self, mock_get):
        """Test GET request failure case."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.ok = False
        mock_get.return_value = mock_response

        self.api.get_post()
        mock_get.assert_called_once()

    ### ✅ POST REQUEST TESTS ###
    @patch("requests.post")
    def test_create_post_success(self, mock_post):
        """Test POST request success case."""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.ok = True
        mock_response.json.return_value = {'userId': 1, 'id': 101, 'title': 'Test', 'body': 'Body'}
        mock_post.return_value = mock_response

        self.api.create_post()
        mock_post.assert_called_once()

    @patch("requests.post")
    def test_create_post_failure(self, mock_post):
        """Test POST request failure case."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.ok = False
        mock_post.return_value = mock_response

        self.api.create_post()
        mock_post.assert_called_once()

    ### ✅ PUT REQUEST TESTS ###
    @patch("requests.put")
    def test_update_post_success(self, mock_put):
        """Test PUT request success case."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.ok = True
        mock_response.json.return_value = {'title': 'Updated Title', 'body': 'Updated Body'}
        mock_put.return_value = mock_response

        self.api.update_post(1)
        mock_put.assert_called_once()

    @patch("requests.put")
    def test_update_post_failure(self, mock_put):
        """Test PUT request failure case."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.ok = False
        mock_put.return_value = mock_response

        self.api.update_post(1)
        mock_put.assert_called_once()

    ### ✅ DELETE REQUEST TESTS ###
    @patch("requests.delete")
    def test_delete_post_success(self, mock_delete):
        """Test DELETE request success case."""
        mock_response = Mock()
        mock_response.status_code = 204  # No content
        mock_response.ok = True
        mock_delete.return_value = mock_response

        self.api.delete_post(1)
        mock_delete.assert_called_once()

    @patch("requests.delete")
    def test_delete_post_failure(self, mock_delete):
        """Test DELETE request failure case."""
        mock_response = Mock()
        mock_response.status_code = 403  # Forbidden
        mock_response.ok = False
        mock_delete.return_value = mock_response

        self.api.delete_post(1)
        mock_delete.assert_called_once()

    ### ✅ GET REQUEST WITH AUTH ###
    @patch("requests.get")
    def test_get_with_basic_auth_success(self, mock_get):
        """Test GET request with Basic Authentication success case."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.ok = True
        mock_response.json.return_value = [{'userId': 1, 'id': 1, 'title': 'Auth Test', 'body': 'Body'}]
        mock_get.return_value = mock_response

        self.api.get_with_basic_auth()
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_get_with_basic_auth_failure(self, mock_get):
        """Test GET request with Basic Authentication failure case."""
        mock_response = Mock()
        mock_response.status_code = 401  # Unauthorized
        mock_response.ok = False
        mock_get.return_value = mock_response

        self.api.get_with_basic_auth()
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2)
