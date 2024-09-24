import requests
import csv
from bs4 import BeautifulSoup

url = 'https://dev.to/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

links = []

for link in soup.find_all('a'):
    links.append(link.get('href'))

# with open('links.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Link"])
#     for link in links:
#         writer.writerow([link])

articles = soup.find_all('h3')

for article in articles:
    title = article.text.strip()
    link = article.find('a')['href']
    publication_date = article.find('time')['datetime']
    print(f"Title: {title}, Link: {link}, Publication Date: {publication_date}")

with open('devto_articles.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Link", "Publication Date"])
    for article in articles:
        title = article.text.strip()
        link = article.find('a')['href']
        publication_date = article.find('time')['datetime']
        writer.writerow([title, link, publication_date])
