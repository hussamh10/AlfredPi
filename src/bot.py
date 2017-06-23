'''
Bot can do the follwoing

'''
import time
import telepot
from urllib import request
import controller
from autonomous_module import AutoModule


def aa():
    return 'haha'

class Bot():
    def __init__(self, telegram):
        self.telegram = telegram
        self.chat_id = None
        self.message_id = 0

    def init_auto_bots(self):
        m = AutoModule(self, aa, 5)
        m.start()

    def init(self):
        print('first')
        self.init_auto_bots()

    def handle(self, message):
        if not self.chat_id:
            self.chat_id = message['chat']['id']
            self.init()

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
        self.telegram.sendMessage(self.chat_id, message)

    def download(self, id, path):
        self.telegram.download_file(id, path)

    def sendImage(self, image):
        image = request.urlopen(image)
        self.telegram.sendPhoto(self.chat_id, ('photo.jpg', image))
