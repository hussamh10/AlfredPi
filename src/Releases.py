import sys
import urllib.request
from bs4 import BeautifulSoup
import google

def getProductURL(product):
    query = product + ' ' + ' site:releases.com'
    result = google.search(query)
    try:
        URL = next(result)
        return URL
    except:
        return None


def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def getStats(url):
    if not url :
        return "Sorry, nothing found."

    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.findAll("div", attrs={"class" : " p-rl-autotext"})

    description = ''
    print(soup)
    description += soup[0].getText(separator=u'$')

    return description

def getReleaseDate(ext):
    product_url = getProductURL(ext)
    print(product_url)
    return getStats(product_url)

