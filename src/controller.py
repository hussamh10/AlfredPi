'''
    ask google
    ask wikipedia
    ask wiki
    ask IMDB
    ask Releases
'''
import Wikipedia
import Wolfram
import Reddit
import Releases
import Google
import IMDB
import Lyrics
from Response import Response
from task_module import TaskModule
from chat_module import ChatModule
from voice_module import VoiceModule

def toString(lst):
    string = ' '
    for s in lst:
        string += s + ' '
    return string[:-1]

def remove(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

def identifyModule(message):
    if('voice' in message.keys()):
        return VoiceModule()
    first = message['text'].split()[0]
    if('ask' == first.lower()):
        return TaskModule()
    chat_modules = ['note', 'remoinder', 'alarm']
    for m in chat_modules:
        if m in message['text']:
            return ChatModule()
    return None
