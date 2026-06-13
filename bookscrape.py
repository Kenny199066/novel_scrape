import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/index.html"

response = requests.get(url)

print(response.status_code)

#print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

cards = soup.select('.product_pod')
#print(cards[0])
all_scraped_books = []
for card in cards:
    title = card.select_one("h3 a").text
    price = card.select_one(".price_color").text

    #print(title, price)

    book_item = {
            "title": title,
            "price": price.replace("£", "")
    } 

    all_scraped_books.append(book_item)

#print(all_scraped_books)

df = pd.DataFrame(all_scraped_books)
#df.to_csv("scraped_books.csv",)

df.to_excel("scraped_books.xlsx",)

