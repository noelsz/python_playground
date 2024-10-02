import requests

from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

quote_items = soup.find_all('div', class_='quote')

quotes = []

for quote_item in quote_items:
    quote = quote_item.find('span', class_='text').text
    author = quote_item.find('small', class_='author').text
    tags = [tag.text for tag in quote_item.find('div', class_='tags').find_all('a', class_='tag')]

    quote_info = {
        'quote': quote,
        'author': author,
        'tags': tags
    }
    quotes.append(quote_info)

for quote in quotes:
    print("Quote: ", quote['quote'])
    print("Author: ", quote['author'])
    print("Tags: ", ', '.join(quote['tags']))
    print()
