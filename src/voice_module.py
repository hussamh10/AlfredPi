from Response import Response
from module import Module

class VoiceModule(Module):

    def playAudio():
        pass

    def performOperation(self, message, bot):
        print(message['voice']['file_id'])
        bot.download(message['voice']['file_id'], 'audio')

        playAudio('audio')
