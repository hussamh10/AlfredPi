import controller
import telepot
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
            self.bot.sendMessages(response.images)
