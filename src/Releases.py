import sys
import urllib.request
from bs4 import BeautifulSoup
from g_search import getUrl

def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def getStats(url):
    if url == 'None' :
        return "Sorry, nothing found."

    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.findAll("div", attrs={"class" : " p-rl-autotext"})

    description = ''
    print(soup)
    description += soup[0].getText(separator=u'$')

    return description

def getReleaseDate(ext):
    product_url = getURL(ext, 'releases.com')
    print(product_url)
    return getStats(product_url)

