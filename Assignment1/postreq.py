import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Learning Web APIs",
    "body": "Practising API requests with Python",
    "userId": 1
}

response = requests.post(url, json=data, timeout=10)

print(response.status_code)
print(response.json())
