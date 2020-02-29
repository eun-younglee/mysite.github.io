#getting artists by web crawling from last.fm
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import os

html = requests.get('https://www.last.fm/user/passionpruit/library/artists?date_preset=ALL')

soup = bs(html.text, 'html.parser')

data1 = soup.find('div', {'class':'col-main'})

data2 = data1.findAll('a', {'class':'link-block-target'})

artists = []
for data3 in data2:
    artists.append(data3.get('title'))

#making them into html files


for i in range(20, len(artists)):
    f = open('{}.html'.format(artists[i]), 'w')
    message = """<!doctype html>
    <html lang="en"><head>
    <title>{}</title>
    <style>
    </style>
    </head>
    <body>
    </body>
    </html>""".format(artists[i])
    f.write(message)
    f.close()

