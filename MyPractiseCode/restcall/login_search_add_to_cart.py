import requests

"""
Explanation of the Authorization Header
Authorization: The header key that tells the server you’re providing credentials for access.
Bearer {token}: The format for token-based authentication, where Bearer indicates the type of token being used,
 followed by the actual token (in this case, token). The token is typically a unique string received from the server 
 after a successful login and serves as proof of identity.
"""


# Define the API endpoints
base_url = "https://example.com/api"  # Replace with the actual server URL
login_endpoint = f"{base_url}/login"
search_endpoint = f"{base_url}/products/search"
add_to_cart_endpoint = f"{base_url}/cart/add"

# User credentials and search term
username = "your-username"
password = "your-password"
search_term = "laptop"  # Replace with the product you're searching for

# Step 1: Log in and obtain a token
login_payload = {
    "username": username,
    "password": password
}

response = requests.post(login_endpoint, json=login_payload)

# Check if login was successful
if response.status_code == 200:
    token = response.json().get("token")  # Assuming token is in JSON response
    headers = {
        "Authorization": f"Bearer {token}"
    }
    print("Login successful!")

    # Step 2: Search for a product
    search_params = {
        "query": search_term
    }
    search_response = requests.get(search_endpoint, headers=headers, params=search_params)

    if search_response.status_code == 200:
        products = search_response.json().get("products", [])

        # Ensure we found products
        if products:
            # Get the first product ID (or choose based on your needs)
            product_id = products[0]["id"]
            print(f"Product found: {products[0]['name']}")

            # Step 3: Add the product to the cart
            cart_payload = {
                "product_id": product_id,
                "quantity": 1
            }
            add_to_cart_response = requests.post(add_to_cart_endpoint, headers=headers, json=cart_payload)
            if add_to_cart_response.status_code == 200:
                print("Product added to cart successfully!")
            else:
                print("Failed to add product to cart:", add_to_cart_response.text)
        else:
            print("No products found for the search term.")
    else:
        print("Search request failed:", search_response.text)
else:
    print("Login failed:", response.text)
