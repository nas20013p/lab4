import httpx

# Base URL of your server
url = "https://cuddly-space-xylophone-5gq6x9jqgwqgh7g56-5000.app.github.dev/"

# Function to make a POST request with given data
def make_post_request(endpoint, data):
    response = httpx.post(url + endpoint, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

# # Data for login
# login_data = {
#     "id": "nazmus.sakib@uconn.edu",
#     "token": "f99aa8b8573062e9802f4fc0807ae1cb"
# }

# Data for successful authorization with different messages
auth_data_success_1 = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb",
}

auth_data_success_2 = {
    "text": "How are you?",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

auth_data_success_3 = {
    "text": "Good morning!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

auth_data_success_4 = {
    "text": "Have a nice day!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

# Data for failed authorization (incorrect token)
auth_data_fail_1 = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "nazmus.sakib@uconn.edu",
    "token": "incorrect_token"
}

auth_data_fail_2 = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value",
    "token_id": "unknown@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

# GET request to the base URL
print("\nRoot Url:")
response = httpx.get(url)
print(f"GET Status Code: {response.status_code}")
print(f"GET Response: {response.text}")

# Login request
print("\nLogin Request:")

# Successful POST requests with different messages
print("\nSuccessful POST Requests:")
make_post_request("login", auth_data_success_1)
make_post_request("login", auth_data_success_2)
make_post_request("login", auth_data_success_3)
make_post_request("login", auth_data_success_4)

# Failed POST requests
print("\nFailed POST Requests:")
make_post_request("login", auth_data_fail_1)
make_post_request("login", auth_data_fail_2)
