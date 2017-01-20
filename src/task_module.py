from Response import Response
from module import Module

import controller
import Wikipedia
import Wolfram
import Reddit
import Releases
import Google
import IMDB
import Lyrics

class TaskModule(Module):

    def handleReddit(operation):
        if 'joke' in operation:
            return Reddit.getJoke()
        if 'hot' in operation or 'daily' in operation:
            return Reddit.getSubreddit('all')
        if 'news' in operation:
            return Reddit.getSubreddit('news')
        if 'subreddit' in operation:
            return Reddit.getSubreddit(operation.split()[-1])

    def generateResponse(self, module, operation):
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

    def parseMessage(self, message):
        module = ''
        operation = []
        ask_modules = ['google', 'wikipedia', 'imdb', 'releases', 'wolfram', 'reddit', 'lyrics']
        parsed = message.split()

        for m in ask_modules:
            if parsed[1] in m:
                module = m
        operation = parsed[2:]
        if operation[0] == 'about':
            operation.remove('about')
        if operation[0] == 'for':
            operation.remove('for')
        operation = self.toString(operation)

        return module, operation

    def performOperation(self, message, bot):
        module, operation = self.parseMessage(message)
        print('debug:' + module + operation)
        response = self.generateResponse(module, operation)

        if response.texts:
            for text in response.texts:
                print(text)
                bot.sendMessage(text)
        if response.images:
            for image_url in response.images:
                bot.sendImage(image_url)

    def toString(self, lst):
        string = ' '
        for s in lst:
            string += s + ' '
        return string[:-1]
