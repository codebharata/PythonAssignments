import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    print(response.json())
else:
    print("Request failed:", response.status_code)
