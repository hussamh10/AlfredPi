import controller
import telepot
from Response import Response
from state import State

class Regular(State):

    def __init__(self, bot):
        self.bot = bot

    def handle(self, message):
        message = message['text']
        print(message)
        module, operation = controller.parseMessage(message)

        response = controller.generateResponse(operation, module)

        if response.texts:
            self.bot.sendMessages(response.texts)
        if response.images:
            for image_url in response.images:
                self.bot.sendImage(image_url)
