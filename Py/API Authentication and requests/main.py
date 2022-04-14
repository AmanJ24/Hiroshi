import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "aman4498"

user_params = {
    "token": "h21ui3h1h32k1j312",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "NotMinor": "yes",
}

# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

requests/post()