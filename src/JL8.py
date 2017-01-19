from urllib import request
import sys
import os

JL8_URL = "http://www.limbero.org/jl8/comics/"

def Download(URL, i, _i):
    path = "C:\\Users\\Hussam\\Documents\\comics\\JL8\\" + str(i) + "_" + str(_i) + ".jpg"
    file = open(path, "wb")
    file.write(URL.read())
    file.close()

def Find_URL(template_url, start, end):

    # The index for downloading
    if end == 0:
        arr = [start]
        else:
        print(start, end)
        arr=list(range(start, end+1))

    for i in arr:
        Extension_exists = True
        Exists = True
        _i = 1
        while Extension_exists:
            if _i == 1: # checks for the first element if the extension exists
                try:
                        image_url = template_url + str(i) + "_" + str(_i) + ".jpeg"
                        res = request.urlopen(image_url)
                        Extension_exists = True
                except :
                        Extension_exists = False
                        Exists = False
            try:
                if Extension_exists:
                        image_url = template_url + str(i) + "_" + str(_i) + ".jpeg"
                else:
                        image_url = template_url + str(i) + ".jpeg"

                res = request.urlopen(image_url)
                Exists = True
            except :
                Exists = False
                Extension_exists = False
            if Exists:
                print(image_url)
                Download(res, i, _i)
            _i += 1


def main(JL8_URL):

    end = 0
    strat = 0
    if len(sys.argv) == 3:
        end = int(sys.argv[-1])
        start = int(sys.argv[-2])
        Find_URL(JL8_URL, start, end=end)
    else:
        start = int(sys.argv[-1])
        Find_URL(JL8_URL, start, end=0)

main(JL8_URL)
