import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
response = requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')
quotes=soup.find_all("span",class_="text")
authors=soup.find_all("small",class_="author")

for quote,author in zip(quotes,authors):
    print(f"{quote.text} - {author.text}")