from Response import Response
from module import Module
import time
import threading

class AutoModule(Module):
    def __init__(self, bot, function, repeat_time, args=None):
        self.stop = False
        self.bot = bot
        self.function = function
        self.repeat_time = repeat_time
        self.args = args

    def start(self):
        thread = threading.Thread(target=self.exec)
        thread.start()

    def kill(self):
        self.stop = True

    def exec(self):
        while(not self.stop):
            message = 'hellobruh'
            if self.args:
                message = self.function(args)
            else:
                message = self.function()

            self.bot.sendMessage('hello')
            time.sleep(self.repeat_time)
