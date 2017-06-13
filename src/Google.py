import urllib.response
import sys

def getUrl(arg):

    url1 = 'https://www.w3.org/services/html2txt?url=https://www.google.com.pk/search?q='
    url2 = '&rlz=1C1NHXL_enPK684PK684&aqs=chrome..69i57.21011j0j1&sourceid=chrome&ie=UTF-8#'

    arg = arg.replace(' ', '%20')
    url = url1+arg+url2
    return url

def getResult(query):

    url = getUrl(query)

    import urllib.request
    with urllib.request.urlopen(url) as response:
        html = response.read()
    html = str(html, 'utf-8')
    html = html.encode(sys.stdout.encoding, errors='ignore')
    html = str(html)
    html = html.split('\\n')
    i = 0
    result = ''

    for line in html:
        if (i > 64 ):
            if ('[' in line):
                break
            if ('[23]Image' in line):
                continue
            if( 'About' in line and 'results' in line):
                continue
            result = result + '\n' + line
        i = i+1
    return result
