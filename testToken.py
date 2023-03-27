import requests

url = "http://0.0.0.0:8001"
headers = {"token": "ff42c5f81bf47e03b141aff91a53020d862d8ada"}
response = requests.get(url, headers=headers)
#response = requests.get(url)

print(response.json())