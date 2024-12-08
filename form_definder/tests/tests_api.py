import requests

BASE_URL = "http://127.0.0.1:8000/api/get_form/"


data = {"data": {"email": "test@example.com", "phone": "+7 123 456 78 90"}}
response = requests.post(BASE_URL, json=data)
print(response.json())


data = {"data": {"unknown_field": "random text"}}
response = requests.post(BASE_URL, json=data)
print(response.json())
