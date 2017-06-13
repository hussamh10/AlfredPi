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
import espeak
import network
import hltr

class TaskModule(Module):

    def handleReddit(self, operation):
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
            response.texts.append(Releases.getReleaseDate(operation))
        if module == 'lyrics':
            response.texts.append(Lyrics.getLyrics(operation))
        if module == 'reddit':
            response.texts = self.handleReddit(operation)
        if module == 'wolfram':
            response.images = Wolfram.getImages(operation)
        if module == 'network':
            response.text = network.scan()
        if module == 'hltr':
            response.texts.append(hltr.getInfo(operation))
        if module == 'espeak':
            espeak.speak(operation)
            response.texts.append('Done, sir')

        if not response.texts and not response.images and not response.audios:
            response.texts = ['I\'m sorry dave, I\'m afraid I can\'t do that']
        return response

    def remove(self, sub, string):
        if string[0] == sub:
            string.remove(sub)


    def parseMessage(self, message):
        module = ''
        operation = []
        ask_modules = ['google', 'wikipedia', 'imdb', 'releases', 'wolfram', 'reddit', 'lyrics', 'espeak', 'network', 'hltr']
        parsed = message.split()

        for m in ask_modules:
            if parsed[1] in m:
                module = m
        operation = parsed[2:]
        self.remove('about', operation)
        self.remove('for', operation)
        self.remove('to', operation)
        operation = self.toString(operation)

        print('debug', module, operation)

        return module, operation

    def performOperation(self, message, bot):
        message = message['text']
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
