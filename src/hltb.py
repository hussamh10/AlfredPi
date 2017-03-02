from bs4 import BeautifulSoup
from g_search import getUrl
from urllib.request import Request, urlopen

def getTimes(p):
    url = getUrl(p, 'howlongtobeat.com')
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    html = urlopen(req)

    soup = BeautifulSoup(html, "html.parser")
    soup = soup.findAll("div", attrs={"class" : "game_times"})

    times = soup[0].text
    return format(times)

def format(times):
    times = times.split('\n')
    times = times[:-8]

    temp = []
    result = []

    for t in times:
        if t.__len__() > 3:
            temp.append(t)

    i = 0
    while i <= 6:
        result.append(temp[i] + ": " + temp[i+1])
        i+=2

    return result
