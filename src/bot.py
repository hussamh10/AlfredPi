'''
Bot can do the follwoing

'''
import telepot
from urllib import request
from regular import Regular

class Bot():
    def __init__(self, telegram):
        self.telegram = telegram
        self.chat_id = None
        self.state = Regular(self)

    def handle(self, message):
        self.chat_id = message['chat']['id']
        self.state.handle(message)

    def sendMessages(self, messages):
        for msg in messages:
            try:
                self.telegram.sendMessage(self.chat_id, msg)
            except:
                self.telegram.sendMessage(self.chat_id, 'I\'m sorry dave, I\'m afraid I can\'t do that')

    def getMessage(self, id=0):
        response = []
        while not response:
            response = self.telegram.getUpdates(id)
        return response[-1]['message']


    def sendMessge(self, message):
            self.telegram.sendMessage(self.chat_id, msg)

    def sendImage(self, image):
        image = request.urlopen(image)
        self.telegram.sendPhoto(self.chat_id, ('photo.jpg', image))
