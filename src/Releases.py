import sys
import urllib.request
from bs4 import BeautifulSoup

def getProductURL(url):
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")
    product_url = soup.find_all('a')[29].get('href')

    print(product_url)
    return product_url

def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def getStats(url):
    if not url :
        return "Sorry, nothing found."

    url = 'http://www.releases.com' + url

    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.findAll("div", attrs={"class" : " p-rl2-item"})

    items = []
    for a in soup:
        items.append(a.getText(separator=u'$'))

    print(items)

    for item in items:
        if ('[Confirmed]' in item):
            item = item.replace('$[Confirmed]', '')
        if ('Track$Track' in item):
            item = item.replace('Track$Track', '')
        if ('-' in item):
            dash_index = find(item, '-')[-1]
            item = item[:dash_index]
        else :
            item = item.rstrip('0123456789$')
            item = item.rstrip('0123456789')
            item = item+'$'
        return item

def getReleaseDate(ext):
    ext = ext.replace(' ', '+')
    main_url = 'http://www.releases.com/search?q='
    url = main_url + ext
    product_url = getProductURL(url)

    return getStats(product_url)
