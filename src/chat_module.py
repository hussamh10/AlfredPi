from module import Module
import Notes
import time

class ChatModule(Module):

    def parseMessage(self, message):
        modules = ['note', 'reminder', 'alarm']
        operations = ['show', 'add', 'remove']

        module = 'None'
        operation = 'None'

        for m in modules:
            if m in message.lower():
                module = m

        for o in operations:
            if o in message.lower():
                operation = o

        return module, operation

    def parseNumbers(self, msg):
        msg = msg.split();
        numbers = []
        for n in msg:
            if n.isdigit():
                numbers.append(int(n))

        return numbers


    def performOperation(self,message, bot):
        module, operation = self.parseMessage(message)
        print('debug:' + module + ' ' + operation)

        bot.sendMessage('Very well sir.')

        if module == 'note':
            if operation == 'add':
                note = bot.getMessage(-1)
                Notes.addNote(note['text'])
                bot.sendMessage('The note has been added.')
            if operation == 'show':
                bot.sendMessage(Notes.getNotes())
            if operation == 'remove':
                msg = bot.getMessage(-1)
                notes = self.parseNumbers(msg['text'])
                Notes.removeNote(notes)
                bot.sendMessage('Removed as requested.')
