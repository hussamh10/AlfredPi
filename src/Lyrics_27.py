'''
    Using the getLyrics function this module takes the artist's name and song's name as input
    and returns a string of lyrics

    Working:
    1. Searches the song
    2. Gets the first reuslt
    3. Parses and returns the lyrics

'''

from bs4 import BeautifulSoup
import urllib2
import google
import sys

def getSoup(URL):
    html = urllib2.urlopen(URL)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def parseSongName(song):            # removes any useless words in song title
    name = ''
    song = song.split()

    delimeters = ['-', '(']
    i = 0

    while i < len(song) and not any(deli in song[i] for deli in delimeters) :
        name += song[i] + ' '
        i+=1

    return name

def getURL(artist, song):
    song = parseSongName(song)
    query = song + ' ' + artist + ' site:azlyrics.com'
    result = google.search(query)
    try:
        URL = next(result)
        return URL
    except:
        return None

def parseLyrics(soup):
    html = soup.prettify()
    html = html.split('\n')
    lyrics = ''
    lyricsText = False

    start = 'third-party lyrics provider'
    end = '</br>'

    for line in html:
        if end in line:
            lyricsText = False
        if lyricsText:
            if '<br>' in line:
                lyrics += '\n'
            else:
                line = line.replace('<i>','')
                line = line.replace('</i>','')
                lyrics += line.strip()
        if start in line:
            lyricsText = True
    return lyrics

def getLyrics(artist, song):
    lyrics = ''

    try:
        URL = getURL(artist, song)
        soup = getSoup(URL)
        lyrics = parseLyrics(soup)
    except Exception as e:
        lyrics = 'Sorry we could not find any lyrics for this song'
    return lyrics

def main():
    title = sys.argv[1]
    print(getLyrics(title, ''))


main()
