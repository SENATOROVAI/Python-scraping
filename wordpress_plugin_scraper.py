import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url: str) -> str:
    return requests.get(url).text

def clean_data(string: str):
    return string.replace(",", "").replace("total ratings", "").strip()

def write_csv(data):
    with open('plugins.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((
                         data['name'],
                         data['url'],
                         data['reviews']
                         ))

def get_data(html: str) -> None:
    soup = BS(html, 'lxml')
    get_plug = soup.find_all(class_='plugin-section')[3]
    plugins = get_plug.find_all('article') 
    
    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        rating = plugin.find('span', class_='rating-count').find('a').text
        clean_rating = clean_data(rating)
        data = {'name': name, 
                'url': url,
                'reviews': clean_rating}
        write_csv(data)
        
def run() -> None:
    url = "https://wordpress.org/plugins/"
    get_data(get_html(url))

if __name__ == '__main__':
    run()

