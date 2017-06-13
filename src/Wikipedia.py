# _*_ coding:utf-8 _*_
import argparse
import sys
import wikipedia
import os

def getSummary(query):
    info = wikipedia.page(query)
    url = info.url
    title = info.title
    content = info.content

    summary = str(wikipedia.summary(query, sentences = 30))
    summary = summary.encode('cp65001')
    summary = str(summary)
    summary =  summary.replace('\\n', os.linesep)

    info = title + os.linesep + url + os.linesep + summary
    return info
