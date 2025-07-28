import unittest
from unittest.mock import Mock, patch

import requests
from requests import get

from unittestcase.rest_call_related.user_data import UserData


class TestUserData(unittest.TestCase):

    def setUp(self):
        self.flow = UserData()

    def test_get_user_data(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.ok = True
        mock_response.json.return_value = {'userId': 1, 'id': 1, 'title': 'Rest Call', 'body': 'quia'}
        get.return_value = mock_response
        self.flow.get_user_data()

    def test_get_user_data_error(self):
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 404
        mock_response.side_effect = Exception
        get.return_value = mock_response
        self.assertRaises(Exception, self.flow.get_user_data)


if __name__ == '__main__':
    unittest.main()
