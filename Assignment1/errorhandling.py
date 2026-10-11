import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)

except requests.exceptions.Timeout:
    print("The request took too long.")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Unable to complete the request:", error)

except ValueError:
    print("Unable to process the JSON response.")
