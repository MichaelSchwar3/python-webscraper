import bs4
import ssl
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
context = ssl._create_unverified_context()
my_url = "http://www.mtggoldfish.com/metagame/standard#paper"

#open the connection, grabbing the page
uClient = uReq(my_url, context=context)

#offloads content into variable
page_html = uClient.read()

#closes connection
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")
#can do things like page_soup.h2 or page_soup.p to see relevant html tags

containers = page_soup.findAll("div", {"class": "archetype-tile"})
percentage = page_soup.findAll("td", {"class": "percentage"})


filename = "mtgdecks.csv"
f = open(filename, 'w')
headers = "deck_name, decks, price, percentage\n"
f.write(headers)
for container in containers:
    deck_name = container.span.text.strip()
    decks = container.table.td.text.strip()
    percentage = container.findAll("td", {"class": "percentage"})[0].text.strip()
    price = container.table.findAll(
        "span", {"class": "deck-price-paper"})[0].text.strip().replace(u'\xa0', u' ')
    print("Deck Name: " + deck_name)
    print("Decks: " + decks)
    print("Price: " + price)
    print("Percentage played: " + price)
    f.write(deck_name + "," + decks + "," + price + "," + percentage + "\n")

f.close()