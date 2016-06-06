import sys
import time
import telepot
import subprocess
import ast
import re
import time
import os

chat_id = 0
module = 0
bot = 0


def downloadTorrent(msg):

    # TODO change dir
    file_name = msg['document']['file_name']
    file_id = msg['document']['file_id']
    dir = 'c:/Users/hussam/Desktop/' + file_name

    bot.download_file(file_id, dir)
    os.system(dir)


def reminderAlert():
    # check if reminder 
    pass


def sendMessage(msg):
    bot.sendMessage(chat_id, msg)


def getStrFromList(string):
    string = str(string, "utf-8")
    list = ast.literal_eval(string)

    return list


def askWolfram(msg):

    msg = msg.lower()

    if ('ask wolfram ' in msg):
        msg = msg.replace ('ask wolfram', '')

    answer = subprocess.check_output(['python', 'Modules\\Wolfram.py', msg])

    
    print (answer)


def askAlfred(msg):
    
    if 'flip' in msg or 'coin' in msg:
        arg = 1

    if 'rps' in msg or 'rock' in msg:
        arg = 2

    answer = subprocess.check_output(['python', 'Modules\\Alfred.py', str(arg)])

    answer = str(answer, 'utf-8')
    
    print (answer)


def getAgenda():

    file = open('Modules\\todo.txt', 'r')
    agenda = file.readlines()

    for line in agenda :
        print(line)
    

def addTodo(msg):

    print('There')
    global module
    module = 'todo'
    subprocess.Popen(['python', 'Modules\\Todo.py', msg])
        
def askTodo(msg):

    global module
    arg = 0

    if 'agenda' in msg:
        arg = 'agenda'
        getAgenda()

    if 'add' in msg:
        module = 'addTodo'

    return 
    

def askWikipedia(msg):
    
    msg = msg.lower()

    if ('ask wiki' in msg):
        msg = msg.replace('ask wiki ', '')

    if ('ask wikipedia' in msg):
        msg = msg.replace('ask wikipedia ', '')

    lines = 5

    if ('detailed' in msg):
        msg = msg.replace('ask wikipedia ', '')
        lines = 0
    
    answer = subprocess.check_output(['python', 'Modules\\Wikipedia.py', msg, '5'])
    answer = getStrFromList(answer)

    string = ''

    sendMessage(answer[2])


def askGoogle(msg):

    msg = msg.lower()

    if ('ask google ' in msg):
        print ('there')
        msg = msg.replace('ask google ', '')

    print ('getting answer for ' + msg)

    msg = msg.split()

    i = 0
    while i < len(msg) - 1:
        msg[i] = msg[i] + '+'
        i += 1

    answer = subprocess.check_output(['python', 'Modules\\Google.py', msg])
    answer = getStrFromList(answer)

    draft = '' 

    for line in answer:
        draft = draft + line

    sendMessage(draft)
    

def askReddit(msg):

    if 'joke' in msg:
        callJoke(msg)
        

def callJoke(msg):
    
    joke_count = 1

    if 'jokes' in msg:
        joke_count = 5
        lst = re.findall('\d+', msg )
        if lst:
            joke_count = int(lst[0])
            if joke_count > 5:
                joke_count = 5
    
    joke = subprocess.check_output(['python', 'Modules\\joke.py', str(joke_count)])
    joke = getStrFromList(joke)

    for j in joke:
        sendMessage(j[0] + '\n - \n' + j[1])


def getModule(msg):

    modules = ['reddit', 'google', 'wikipedia', 'wiki', 'alfred', 'wolfram', 'todo']
    
    for module in modules:
        if module in msg.lower():
            return module
    return 0
    

def HandleText(msg):

    global module
    
    temp_module = getModule(msg)

    if temp_module != 0:
        module = temp_module

    print (module )
     
    if module == 'reddit':
        askReddit(msg)
    if module == 'google':
        askGoogle(msg)
    if module == 'wikipedia' or module == 'wiki':
        askWikipedia(msg)
    if module == 'alfred':
        askAlfred(msg)
    if module == 'wolfram':
        askWolfram(msg)
    if module == 'todo':
        askTodo(msg)
    if module == 'addTodo':
        addTodo(msg)
        

def handle(msg):

    global chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)

    print (content_type)
    print (msg)
    if (content_type == 'text'):
        HandleText(msg['text'])

    if (content_type == 'photo'):
        pass

    if (content_type == 'document'):
        if '.torrent' in msg['document']['file_name']:
            downloadTorrent(msg)
        


def handleEvents():
    
    if reminderAlert():
        # send reminder
        pass
    

def main(): 

    global bot

    bot = telepot.Bot('BOT ID HERE')
    bot.message_loop(handle)

    while True:
        handleEvents()
        pass
    

main()
