import requests

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print(content)
else:
    print(f"Error: {response.status_code}")

# This script sends a GET request to the URL specified by the url variable using the requests.get() method. It then checks the status code of the response to ensure that the request was successful. If the status code is 200, indicating success, the script prints the content of the response using the response.text attribute.

# Of course, this is just a very basic example of web scraping using requests. Depending on the website and the data you want to scrape, you may need to use additional libraries or techniques to successfully extract the desired information. Additionally, it's important to be aware of the legal and ethical considerations surrounding web scraping.

