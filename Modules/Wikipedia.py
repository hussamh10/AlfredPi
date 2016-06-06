# _*_ coding:utf-8 _*_
import argparse
import sys
import wikipedia

# Takes 2 args : a string that is to be searched & the number of lines to be printed (0=default)
# Returns a list [title, url, summary] 

def main():

    arg_count = len(sys.argv) - 2
    string = ''

    for i in range(0, arg_count):
        string = string + ' ' + sys.argv[i+1]
    	
    count = int(sys.argv[-1])
        
    string = string[1:] 

    info = wikipedia.page(string)
    url = info.url
    title = info.title
    content = info.content

    if count == 0 :
        summary = str(wikipedia.summary(string))
    else:
        summary = str(wikipedia.summary(string, sentences=count))


    summary.encode('ascii', 'ignore')
    summary = summary.encode(sys.stdout.encoding, errors='ignore')

    content.encode('ascii', 'ignore')
    content = content.encode(sys.stdout.encoding, errors='ignore')


    list = [title, url, summary] # can add content

    print (str(list))

main()
