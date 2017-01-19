import wolframalpha
import sys
import pprint

def getImages(string):
    client = wolframalpha.Client('PGQ3TL-EXWG2EA68R')
    res = client.query(string)

    imgs = []
    for pod in res.pods:
        for sub in pod.subpods:
            for img in sub.img:
                imgs.append(img['@src'])
    return imgs
