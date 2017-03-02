from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from g_search import getUrl


def getInfo(p):
    url = getUrl(p, 'howlongtoreadthis.com')

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    html = urlopen(req)

    soup = BeautifulSoup(html, "html.parser")
    soup = soup.findAll("h2", attrs={"class" : "book-details"})

    return soup[0].text
