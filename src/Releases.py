import sys
import urllib.request
from bs4 import BeautifulSoup

def getProductURL(url):
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")

    product_url = soup.find_all('a')#[104].get('href')
    for p in product_url:
        if '/p/' in p.get('href'):
            return p.get('href')

    ##return product_url


def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def getStats(url):
    if not url :
        return "Sorry, nothing found."

    url = 'http://www.releases.com' + url
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.findAll("div", attrs={"class" : " p-rl-autotext"})

    description = ''
    print(soup)
    description += soup[0].getText(separator=u'$')

    return description

def getReleaseDate(ext):
    ext = ext.replace(' ', '%20')
    main_url = 'http://www.releases.com/search?q='
    url = main_url + ext
    print(url)

    product_url = getProductURL(url)

    print(product_url)

    return getStats(product_url)
