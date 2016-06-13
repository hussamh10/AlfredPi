import datetime
import pprint
import sys
import telepot
import subprocess
import ast
import re
import time
import os
import urllib.request

chat_id = 0
module = 0
bot = 0


def remReminder():

    getAgenda()
    sendMessage('Which reminder would you like to remove?')

    response = bot.getUpdates()

    id = int(response[0]['update_id'])

    response = []
    id = id+1
    
    while not response:
        response = bot.getUpdates(id)
        if response :
            number = (response[0]['message']['text'])

    global module
    module = 'alfred'
    subprocess.Popen(['python', 'Modules\\Todo.py', number, '0'])


def getDateTime(id):

    today = datetime.datetime.now()
    date = [0, 0, 0]
    date[0] = today.day
    date[1] = today.month
    date[2] = today.year

    time = [0,0]
    time[0] = today.hour
    time[1] = today.minute

    hide_keyboard = {'hide_keyboard': True}
    quick_date_kbrd = {'keyboard': [['Today', 'Tomorrow', 'No'], ['Enter Date', 'Enter Month', 'Enter Year']]}
    bot.sendMessage(chat_id, 'At what Day', reply_markup=quick_date_kbrd)

    id = id+1

    response = []

    while not response:
        response = bot.getUpdates(id)
        
        if response :
            quick_date = str(response[0]['message']['text'])
            bot.sendMessage(chat_id, 'Hiding it now.', reply_markup=hide_keyboard)

    if quick_date == 'No':
        return date, time

    if (quick_date == 'Today'):
        today = datetime.datetime.now()
        date[0] = today.day
        date[1] = today.month
        date[2] = today.year

    if (quick_date == 'Tomorrow'):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        date[0] = tomorrow.day
        date[1] = tomorrow.month
        date[2] = tomorrow.year

    if quick_date == 'Enter Year':
        year_kbrd = {'keyboard': [['2016', '2017']]}
        bot.sendMessage(chat_id, 'At what Year', reply_markup=year_kbrd)

        id = id+1

        response = []

        while not response:
            response = bot.getUpdates(id)

            if response :
                year = str(response[0]['message']['text'])
                bot.sendMessage(chat_id, 'Hiding it now.', reply_markup=hide_keyboard)

        date[2] = int(year)
        quick_date = 'Enter Month'

    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                    
    if quick_date == 'Enter Month':

        
        month_kbrd = {'keyboard': [list[:6], list[6:12]]}
        bot.sendMessage(chat_id, 'At what Month', reply_markup=month_kbrd)

        id = id+1

        response = []

        while not response:
            response = bot.getUpdates(id)
            if response :
                month = str(response[0]['message']['text'])
                bot.sendMessage(chat_id, 'Hiding it now.', reply_markup=hide_keyboard)

        date[1] = int(month)
        quick_date = 'Enter Date'

    if quick_date == 'Enter Date':

        date_kbrd = {'keyboard': [list[:11], list[11:21], list[21:31]]}
        bot.sendMessage(chat_id, 'At what Date', reply_markup=date_kbrd)

        id = id+1

        response = []

        while not response:
            response = bot.getUpdates(id)
            if response :
                day = str(response[0]['message']['text'])
                bot.sendMessage(chat_id, 'Hiding it now.', reply_markup=hide_keyboard)

        date[0] = int(day)
        

    # Enter Time

    bot.sendMessage(chat_id, 'Enter Time')
    
    id = id+1
    entered_time = 0

    response = []
    
    while not response:
        response = bot.getUpdates(id)
        if response :
            entered_time = str(response[0]['message']['text'])

    if 'm' in entered_time:
        # am / pm
        if 'am' in entered_time:
            entered_time = entered_time.replace('am', '')
            eentered_time = entered_time.split(':')
            entered_time[0] = int(entered_time[0])
            entered_time[1] = int(entered_time[1])
            
        if 'pm' in entered_time:
            entered_time = entered_time.replace('pm', '')
            entered_time = entered_time.split(':')
            entered_time[0] = int(entered_time[0])
            entered_time[1] = int(entered_time[1])
            entered_time[0] += 12

    else:
        entered_time = entered_time.split(':')
        entered_time[0] = int(entered_time[0])
        entered_time[1] = int(entered_time[1])

    time[0] = entered_time[0]
    time[1] = entered_time[1]

    print(date, time)
    return date, time
    
def addReminder():

    time = ''
    reminder = ''

    response = bot.getUpdates()

    id = int(response[0]['update_id'])

    response = []
    sendMessage('What would you like to add?')

    id = id+1
    
    while not response:
        response = bot.getUpdates(id)
        if response :
            reminder = (response[0]['message']['text'])
    
    (date, time) = getDateTime(id)

    epoch = changeToEpoch(date_time)

    print (time + reminder)

    msg = (time + reminder)

    global module
    module = 'alfred'
    subprocess.Popen(['python', 'Modules\\Todo.py', msg, '1'])
        

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

def chatAction(msg):
    bot.sendChatAction(chat_id, msg)


def getStrFromList(string):
    string = str(string, "utf-8")
    list = ast.literal_eval(string)

    return list


def askDictionary(msg):

    msg = msg.lower()
    
    if ('ask dict ' in msg):
        msg = msg.replace ('ask dict ', '')
    if ('ask dictionary' in msg):
        msg = msg.replace ('ask dictionary ', '')
    if ('define ' in msg):
        msg = msg.replace ('define ', '')

    answer = subprocess.check_output(['python', 'Modules\\Dictoinary.py', msg])
    
    print (answer)


def askWolfram(msg):

    msg = msg.lower()

    if ('ask wolfram ' in msg):
        msg = msg.replace ('ask wolfram', '')

    answer = subprocess.check_output(['python', 'Modules\\Wolfram.py', msg])
    answer = getStrFromList(answer)

    
    print (answer)


def askAlfred(msg):
    
    global module
    
    if 'flip' in msg or 'coin' in msg:
        arg = 1
        answer = subprocess.check_output(['python', 'Modules\\Alfred.py', str(arg)])
        answer = str(answer, 'utf-8')
        sendMessage (answer)

    if 'rps' in msg or 'rock' in msg:
        arg = 2

    if 'agenda' in msg:
        getAgenda()

    if 'add' in msg and 'reminder' in msg:
        addReminder()
    
    if 'remove' in msg and 'reminder' in msg:
        remReminder()


def getAgenda():

    file = open('todo.txt', 'r')
    agenda = file.readlines()

    i = 0

    for line in agenda :
        i += 1
        sendMessage(str(i) + '. ' + line)
    

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

    chatAction('typing')
        
    answer = subprocess.check_output(['python', 'Modules\\Wikipedia.py', msg, '5'])
    answer = str(answer, 'utf-8')

    summary =''
    
    for a in answer:
        summary = summary + str(a)
    
    summary = summary.replace('\\'+'x96', '-')
    summary = summary.replace('\\' +'\'', '\'')
    summary = summary.replace('\\' +'n', '')

    content = summary.splitlines()
    
    sendMessage(content[1])
    sendMessage(content[0][2:-1])

def askGoogle(msg):

    msg = msg.lower()

    if ('ask google ' in msg):
        msg = msg.replace('ask google ', '')


    msg = msg.split()

    i = 0
    while i < len(msg) - 1:
        msg[i] = msg[i] + '+'
        i += 1

    url = 'https://www.google.com.pk/search?q='

    for i in msg:
        url = url + i

    chatAction('typing')

    answer = subprocess.check_output(['python', 'Modules\\Google.py', msg])
    answer = getStrFromList(answer)

    draft = '' 

    for line in answer:
        draft = draft + '\n' +  line

    sendMessage(url + '\n' )
    sendMessage(draft)
    

def askReddit(msg):

    if 'joke' in msg:
        callJoke(msg)
    elif 'fact' in msg:
        pass
        #callMessage(msg)
        

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

    modules = ['reddit', 'google', 'wikipedia', 'wiki', 'alfred', 'wolfram']
    
    for module in modules:
        if module in msg.lower():
            return module
    return 0
    

def HandleText(msg):

    global module
    
    temp_module = getModule(msg)

    if temp_module != 0:
        module = temp_module

    print (module)
     
    if module == 'reddit':
        askReddit(msg)
    elif module == 'google':
        askGoogle(msg)
    elif module == 'wikipedia' or module == 'wiki':
        askWikipedia(msg)
    elif module == 'alfred':
        askAlfred(msg)
    elif module == 'wolfram':
        askWolfram(msg)
        

def handle(msg):

    global chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)

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

    bot = telepot.Bot('232702502:AAFEUh-lDo1vb641bOJ_fJ2ar-LsVM0zeO4')
    bot.message_loop(handle)

    while True:
        pass
    

main()
