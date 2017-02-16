'''
Bot can do the follwoing

'''
import time
import telepot
from urllib import request
import controller

class Bot():
    def __init__(self, telegram):
        self.telegram = telegram
        self.chat_id = None
        self.message_id = 0

    def handle(self, message):
        self.chat_id = message['chat']['id']
        message_id = message['message_id']

        if self.message_id >= message_id:
            return

        self.message_id = message_id

        module = controller.identifyModule(message)

        if module is None:
            self.sendMessage('Sorry sir, I can\'t understand you')
            return

        module.performOperation(message, self)

    def getMessage(self, id=-1):
        response = []
        message = ''
        while True:
            response = self.telegram.getUpdates(99999999999999)

            if response:
                message_id = response[-1]['message']['message_id']
                if message_id > self.message_id:
                    self.message_id = message_id
                    return response[-1]['message']

    def sendMessage(self, message):
        try:
            self.telegram.sendMessage(self.chat_id, message)
        except:
            self.telegram.sendMessage(self.chat_id, 'I\'m sorry dave, I\'m afraid I can\'t do that (Error while sending)')

    def download(self, id, path):
        self.telegram.download_file(id, path)

    def sendImage(self, image):
        image = request.urlopen(image)
        self.telegram.sendPhoto(self.chat_id, ('photo.jpg', image))
