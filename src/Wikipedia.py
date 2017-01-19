# _*_ coding:utf-8 _*_
import argparse
import sys
import wikipedia

def getSummary(query):
    info = wikipedia.page(query)
    url = info.url
    title = info.title
    content = info.content

    summary = str(wikipedia.summary(query, sentences = 30))


    info = [title, url, summary] # can add content
    return info
