#programme that downloads all the albums from the artist you type 
from bs4 import BeautifulSoup as bs
import requests
import wget
import os

url = 'https://en.wikipedia.org/wiki/Meddle'

def title(address):
    html = requests.get(address)
    soup = bs(html.text, 'html.parser')
    data1 = soup.find('table', {'class':'wikitable'})
    albums = []
    urls = []
    for data2 in data1.findAll('i'):
        data3 = data2.find('a')
        albums.append(data3.get_text('title'))
        urls.append(data3.get('href'))
    return albums

def url(address):
    html = requests.get(address)
    soup = bs(html.text, 'html.parser')
    data1 = soup.find('table', {'class':'wikitable'})
    albums = []
    urls = []
    for data2 in data1.findAll('i'):
        data3 = data2.find('a')
        albums.append(data3.get_text('title'))
        urls.append(data3.get('href'))
    return urls 

def cover(addr):
    content = requests.get(addr).content
    soup = bs(content,'lxml')
    image = soup.find('td', {'colspan':'2'})
    im = image.find('img')
    pic = im.get('srcset')
    pic = '{}{}'.format("https:", pic)
    pic = pic.replace(" 1.5x", "")
    wget.download(pic, 'D:\source\web\Albums')

    #if there's no url, print cannot find url (try / except)

while(True):
    print('\n\nWhose discography do you want?(Every first letter has to be a capital, Type q to quit)', end = ': ')
    n = input()
    n = n.replace(" ", "_")
    if(n == 'q'):
        break
    else:
        wiki = 'https://en.wikipedia.org/wiki/{}_discography'.format(n)
        alb = []
        alb = title(wiki)
        for i in range(len(alb)):
            print("\n")
            link = url(wiki)
            links = "https://en.wikipedia.org{}".format(link[i])
            print(alb[i])
            try:
                cover(links)
            except:
                print("Cannot download the album")
                continue 
