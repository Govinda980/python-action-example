import concurrent.futures
import requests

# List of API endpoints
urls = ['https://jsonplaceholder.typicode.com/posts','https://jsonplaceholder.typicode.com/comments']


def fetch_data(url):
    response = requests.get(url)
    return response.json()  # or response.text depending on your API's response format


try:
    # Use ThreadPoolExecutor to run API calls in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_data, urls))
except Exception as e:
    print(e)

# Process the results
for result in results:
    print(result)
