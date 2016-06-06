import urllib.response
import sys

def getUrl():

    url1 = 'https://www.w3.org/services/html2txt?url=https://www.google.com.pk/search?q='
    url2 = '&rlz=1C1NHXL_enPK684PK684&aqs=chrome..69i57.21011j0j1&sourceid=chrome&ie=UTF-8#'
    
    arg_count = len(sys.argv) - 1
    string = ''

    for i in range(0, arg_count):
        string = string + '+' + sys.argv[i+1]
    string = string[1:]
        
    url = url1+string+url2
    return url

def main():

    url = getUrl()

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
            if ('[' in line and i > 66):
                break
            if ('[23]Image' in line):
                continue
            
            result = result + '\n' + line
        i = i+1
    
    result = result.splitlines()

    print (result)
        
main ()
