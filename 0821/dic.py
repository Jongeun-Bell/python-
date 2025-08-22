import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)
print(response)

if response.status_code == 200:
    data = response.json()

    