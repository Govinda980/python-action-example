import requests


def get_user_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


