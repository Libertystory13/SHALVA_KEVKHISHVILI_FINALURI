from bs4 import BeautifulSoup
import requests
import json

x = requests.get("http://quotes.toscrape.com/author/Albert-Einstein/?fbclid=IwAR2DI42BJBiLV29VHw-XOgAfBPrxpIo5inh1C1ud-nCqlTbKo9XjzJg1r9Y")
soup = BeautifulSoup(x.text, 'lxml')
name = soup.select_one('[class^="author-title"]').text
born = ""
year = soup.select_one('[class^="author-born-date"]').text
place = soup.select_one('[class^="author-born-location"]').text
born += year +" " +place
description = soup.select_one('[class^="author-description"]').text


data = {"name": name, "born": born, "descirption": description }
with open('data.json', 'w') as f:

    json.dump(data, f)