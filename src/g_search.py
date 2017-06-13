import google

def getUrl(q, site):
    query = p + ' site:' + site
    result = google.search(query)
    try:
        URL = next(result)
        print(URL)
        return URL
    except:
        print("None")
        return None

