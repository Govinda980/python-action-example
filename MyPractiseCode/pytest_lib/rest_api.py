import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

assert response.status_code == 200  # Check if the response is OK
print(response.json())  # Print response data




def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()["id"] == 1
