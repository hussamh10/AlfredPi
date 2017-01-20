'''
    ask google
    ask wikipedia
    ask wiki
    ask IMDB
    ask Releases
'''
import Wikipedia
import Wolfram
import Reddit
import Releases
import Google
import IMDB
import Lyrics
from Response import Response
from task_module import TaskModule

def toString(lst):
    string = ' '
    for s in lst:
        string += s + ' '
    return string[:-1]

def remove(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

def identifyModule(message):
    if('ask' == message['text'].split()[0]):
        return TaskModule()

def handleReddit(operation):
    if 'joke' in operation:
        return Reddit.getJoke()
    if 'hot' in operation or 'daily' in operation:
        return Reddit.getSubreddit('all')
    if 'news' in operation:
        return Reddit.getSubreddit('news')
    if 'subreddit' in operation:
        return Reddit.getSubreddit(operation.split()[-1])

def parseMessage(message):
    module = ''
    operation = []
    ask_modules = ['google', 'wikipedia', 'imdb', 'releases', 'wolfram', 'reddit']
    add_modules = ['note', 'reminder', 'alarm']
    parsed = message.split()
    if 'lyrics' in parsed:
        module = 'lyrics'
        operation = parsed
        operation = remove(operation, 'get')
        operation = remove(operation, 'lyrics')
        operation = remove(operation, 'for')
        operation = toString(operation)

    elif parsed[0] == 'ask':
        for m in ask_modules:
            if parsed[1] in m:
                module = m
        operation = parsed[2:]
        if operation[0] == 'about':
            operation.remove('about')
        if operation[0] == 'for':
            operation.remove('for')
        operation = toString(operation)

    else:
        module = 'alfred'

    return module, operation

def generateResponse(operation, module):
    response = Response()
    if module == 'google':
        response.texts.append(Google.getResult(operation))
    if module == 'wikipedia':
        response.texts.append(Wikipedia.getSummary(operation))
    if module == 'imdb':
        response.texts = IMDB.getMovieInfo(operation)
    if module == 'releases':
        response.texts = None
    if module == 'lyrics':
        response.texts.append(Lyrics.getLyrics(operation))
    if module == 'reddit':
        response.texts = handleReddit(operation)
    if module == 'wolfram':
        response.images = Wolfram.getImages(operation)

    if not response.texts and not response.images and not response.audios:
        response.texts = ['I\'m sorry dave, I\'m afraid I can\'t do that']
    return response
