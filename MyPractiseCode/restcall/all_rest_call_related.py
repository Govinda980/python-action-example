import requests

# API Credentials & Configuration
BEARER_TOKEN = "Token_name"
USER_NAME = "Govinda"
USER_PASSWORD = "Test@123"
API_KEY = "Api_keys"
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Headers with Authentication
HEADERS = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json',
}


class RestOperation:
    """Class to perform REST API operations."""

    def get_post(self):
        """Perform a GET request to fetch posts."""
        response = requests.get(BASE_URL, headers=HEADERS)
        if response.status_code == 200:
            res_data = response.json()[:1]
            print("GET Response:", res_data)
        else:
            print(f"GET Request failed with status code: {response.status_code}")

    def create_post(self):
        """Perform a POST request to create a new post."""
        data = {
            "title": "Riyansh is the King!",
            "body": "Riyansh is a Hero",
            "userId": 1
        }
        response = requests.post(BASE_URL, headers=HEADERS, json=data)
        if response.status_code == 201:
            res_data = response.json()
            print(f"POST Response: {res_data}")
        else:
            print(f"POST Request failed with status code: {response.status_code}")

    def update_post(self, post_id):
        """Perform a PUT request to update a post."""
        data = {
            "title": "Riyansh is the King!",
            "body": "Riyansh is a Super Hero",
        }
        response = requests.put(f'{BASE_URL}/{post_id}', json=data, headers=HEADERS)
        if response.status_code == 200:
            print("PUT Response:", response.json())
        else:
            print(f"PUT Request failed with status code: {response.status_code}")

    def delete_post(self, post_id):
        """Perform a DELETE request to remove a post."""
        response = requests.delete(f'{BASE_URL}/{post_id}', headers=HEADERS)
        if response.status_code in [200, 204]:  # Check for both 200 & 204 (No Content)
            print("DELETE Successful")
        else:
            print(f"DELETE Request failed with status code: {response.status_code}")

    def get_with_basic_auth(self):
        """Perform a GET request with basic authentication."""
        response = requests.get(BASE_URL, auth=(USER_NAME, USER_PASSWORD))
        if response.status_code == 200:
            print("Basic Auth Response:", response.json()[:2])
        else:
            print(f"Basic Auth Request failed with status code: {response.status_code}")


# ✅ Running API Calls
if __name__ == '__main__':
    api = RestOperation()
    api.get_post()
    api.create_post()
    api.update_post(1)
    api.delete_post(1)
    api.get_with_basic_auth()
