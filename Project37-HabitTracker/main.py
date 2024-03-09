import requests
from datetime import datetime

TOKEN = "Abc123456"
USERNAME = "proakash256"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# The above line is needed only one time, to create the user.

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
# Normally, we give our API Key, to authenticate ourselves along with the parameters,
# but that is an unsafe way. To do it in a more secure way, we use headers.
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)

# To post a pixel
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.5"
}
pixel_response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)

# To update a pixel
PIXEL_UPDATE_ENDPOINT = f"{PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}"
pixel_update_params = {
    "quantity": "20.0"
}
pixel_update_response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=pixel_update_params, headers=headers)

# To delete pixel
PIXEL_DELETE_ENDPOINT = f"{PIXEL_ENDPOINT}/20230324"
pixel_delete_response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
