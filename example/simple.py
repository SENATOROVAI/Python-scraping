import requests

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print(content)
else:
    print(f"Error: {response.status_code}")
