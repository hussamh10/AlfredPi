#TODO change dir in openFile
#TODO sendPhoto in askComic

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
NO_TIME = 9999999999

def createWeekPlan():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 

    response = bot.getUpdates()
    id = int(response[0]['update_id'])
    id += 1
    task = ''
    plan = []
    i = 0
    dayPlan = []

    while (i < 7):
        sendMessage('Add tasks for ' + days[i] + '.')
        while task.lower() != 'end':
            task = getMessage(id)[0][0]
            dayPlan.append(task)
            id += 1
            print(task)
        plan.append(dayPlan[:-1])
        dayPlan = []
        task = ''    
        i += 1    

    string = ''
    file = open('plan', 'w')

    i = 0
    for day in plan:
        string = string + '--------------' + days[i] + '--------------$'
        for task in day:
            string = string + task + '$'
        string = string + '\n'    

    file.write(string)



def getMessage(id=0):
    if id == 0:
        response = bot.getUpdates()
        id = int(response[0]['update_id'])
        id += 1

    response = []
    while not response:
        response = bot.getUpdates(id)

    return [response[0]['message']['text']],[ id]

def playAudio(msg):
    dir = 'c:/Users/hussam/Desktop/' + 'audio.ogg'
    file_id = msg['voice']['file_id']
    #bot.download_file(file_id, dir)

    os.system(dir)

def askReleases(msg):
    msg = msg.lower()

    list = getMessage()
    id = list[1]
    response = list[0]

    print(response[0])
    return 

    if 'ask releases ' in msg:
        msg = msg.replace('ask releases ', '')
    if 'ask release ' in msg:
        msg = msg.replace('ask release ', '')

    print(msg)
    answer = subprocess.check_output(['python3', 'Modules/Releases.py', msg])
    answer = str(answer, 'utf-8')
    answer = answer.replace('$' , '\n')

    sendMessage(answer)

def askComic(msg):
    msg = msg.lower()
    if 'jl8' in msg:
       msg = msg.replace('jl8', '')

    lst = re.findall('\d+', msg )
    if lst:
        if len(lst) == 2:
            answer = subprocess.check_output(['python3', 'Modules/JL8.py', str(lst[0]), str(lst[1])])
            answer = str(answer, 'ascii')
        else:
            answer = subprocess.check_output(['python3', 'Modules/JL8.py', str(lst[0])])
            answer = str(answer, 'ascii')
    else :
        answer = subprocess.check_output(['python3', 'Modules/JL8.py', '1'])
        answer = str(answer, 'ascii')
        print(answer)

def askSleep(module, msg):
    if module == 'wake':
        sendMessage('When would you like to wake, sir?')

    if module == 'sleep':
        sendMessage('When are you going to sleep, sir?')

    today = datetime.datetime.now()
    date = [0, 0, 0]
    date[0] = today.day
    date[1] = today.month
    date[2] = today.year

    time = [0,0]
    time[0] = today.hour
    time[1] = today.minute

    response = bot.getUpdates()
    id = int(response[0]['update_id'])
    id += 1

    hide_keyboard = {'hide_keyboard': True}
    quick_date_kbrd = {'keyboard': [['Today', 'Tomorrow']]}
    bot.sendMessage(chat_id, 'When, sir?', reply_markup=quick_date_kbrd)

    response = getMessage(id)[0][0]

    bot.sendMessage(chat_id, 'Got it.', reply_markup=hide_keyboard)
    id += 1
    d = response

    # Enter Time

    bot.sendMessage(chat_id, 'Enter Time')

    entered_time = 0

    entered_time = getMessage(id)[0][0]

    if 'm' in entered_time:
        # am / pm
        if 'am' in entered_time:
            entered_time = entered_time.replace('am', '')
            entered_time = entered_time.split(':')
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

    if 'Tomorrow' in d:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        date[0] = tomorrow.day
        date[1] = tomorrow.month
        date[2] = tomorrow.year


    epoch = changeToEpoch(date, time)

    if module == 'wake':
        answer = subprocess.check_output(['python3', 'Modules/Sleep.py', 0, int(epoch)])
        answer = getStrFromList(answer)
        print (answer) 

    if module == 'sleep':

        answer = subprocess.check_output(['python3', 'Modules/Sleep.py', 1, int(epoch)])
        answer = getStrFromList(answer)
        print (answer)

def addNote():
    note = ''

    response = bot.getUpdates()[0][0]

    id = int(response[0]['update_id'])

    response = []
    sendMessage('What would you like to add, sir?')

    id = id+1
    
    response = getMessage(id)[0][0]

    global module
    module = 'alfred'

    subprocess.Popen(['python3', 'Modules/Notes.py', note, '1'])

def remNote():
    getNotes()
    sendMessage('Which note would you like to remove?')

    response = bot.getUpdates()

    id = int(response[0]['update_id'])
    id = id+1

    response = bot.getUpdates(id)[0][0]

    global module
    module = 'alfred'
    subprocess.Popen(['python3', 'Modules/Notes.py', number, '0'])

    sendMessage('Reminder removed')

def getNotes():
    file = open('notes.txt', 'r')
    agenda = file.readlines()

    i = 0

    for line in agenda :
        i += 1
        line = line.replace('$', '\n')
        sendMessage(str(i) + '. ' + line)

def remReminder():
    getAgenda()
    sendMessage('Which reminder would you like to remove?')

    response = bot.getUpdates()

    id = int(response[0]['update_id'])

    response = []
    id = id+1
    
    response = getMessage(id)[0][0]

    global module
    module = 'alfred'
    subprocess.Popen(['python3', 'Modules/Todo.py', number, '0'])

def changeToEpoch(date, time):
    if not date:
        return 9999999999.0

    epoch = datetime.datetime(date[2], date[1], date[0], time[0], time[1]).timestamp()
    epoch = epoch - 10800
    return epoch

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

    quick_date = getMessage(id)[0][0]
    bot.sendMessage(chat_id, 'Got it.', reply_markup=hide_keyboard)

    if quick_date == 'No':
        return ([], [])

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

        year = getMessage(id)[0][0]
        bot.sendMessage(chat_id, 'Got it', reply_markup=hide_keyboard)

        date[2] = int(year)
        quick_date = 'Enter Month'

    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
                    
    if quick_date == 'Enter Month':

        
        month_kbrd = {'keyboard': [list[:6], list[6:12]]}
        bot.sendMessage(chat_id, 'At what Month', reply_markup=month_kbrd)

        id = id+1

        month = getMessage(id)[0][0]
        bot.sendMessage(chat_id, 'Got it', reply_markup=hide_keyboard)

        date[1] = int(month)
        quick_date = 'Enter Date'

    if quick_date == 'Enter Date':

        date_kbrd = {'keyboard': [list[:11], list[11:21], list[21:31]]}
        bot.sendMessage(chat_id, 'At what Date', reply_markup=date_kbrd)

        id = id+1

        day = getMessage(id)[0][0]
        bot.sendMessage(chat_id, 'Got it', reply_markup=hide_keyboard)

        date[0] = int(day)
        

    # Enter Time

    bot.sendMessage(chat_id, 'Enter Time')
    
    id = id+1
    entered_time = 0

    entered_time = getMessage(id)[0][0]

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

    return date, time
    
def addReminder():
    time = ''
    reminder = ''

    response = bot.getUpdates()

    id = int(response[0]['update_id'])

    response = []
    sendMessage('What would you like to add, sir?')

    id = id+1
    
    reminder = getMessage(id)[0][0]
    
    (date, time) = getDateTime(id)

    epoch = changeToEpoch(date, time)

    msg = (reminder + ' ' + str(epoch))

    sendMessage('Your reminder has been added sir.')

    global module
    module = 'alfred'
    subprocess.Popen(['python3', 'Modules/Todo.py', msg, '1'])

def openFile(msg, pre=''):
    file_name = msg['document']['file_name']
    file_id = msg['document']['file_id']
    dir = 'c:/Users/hussam/Desktop/' + file_name

    print('there')

    #TODO bot.download_file(file_id, dir)

    print('here')

    if not pre:
        os.system(dir)
    else:
        sendMessage(str(os.popen('python3' + ' ' + dir).read()))

def sendMessage(msg):
    bot.sendMessage(chat_id, msg)
    return

def chatAction(msg):
    bot.sendChatAction(chat_id, msg)
    return

def getStrFromList(string):
    try :
        string = str(string, "utf-8")
        list = ast.literal_eval(string)
    except Exception as e:
        list = [['Error', 'from getStrFromList']]

    return list

def askDictionary(msg):
    msg = msg.lower()
    
    if ('ask dict ' in msg):
        msg = msg.replace ('ask dict ', '')
    if ('ask dictionary' in msg):
        msg = msg.replace ('ask dictionary ', '')
    if ('define ' in msg):
        msg = msg.replace ('define ', '')

    answer = subprocess.check_output(['python3', 'Modules/Dictoinary.py', msg])
    
    print (answer)

def askWolfram(msg):
    msg = msg.lower()

    if ('ask wolfram ' in msg):
        msg = msg.replace ('ask wolfram', '')

    answer = subprocess.check_output(['python3', 'Modules/Wolfram.py', msg])
    answer = getStrFromList(answer)

    
    print (answer)

def askAlfred(msg):
    global module
    msg = msg.lower()
    
    if 'flip' in msg or 'coin' in msg:
        arg = 1
        answer = subprocess.check_output(['python3', 'Modules/Alfred.py', str(arg)])
        answer = str(answer, 'utf-8')
        sendMessage (answer)

    elif 'rps' in msg or 'rock' in msg:
        arg = 2

    elif 'agenda' in msg:
        getAgenda()

    elif 'note' in msg and'show' in msg:
        getNotes()

    elif 'add' in msg and 'rem' in msg:
        addReminder()
    
    elif 'remove' in msg and 'reminder' in msg:
        remReminder()

    elif 'add' in msg and 'note' in msg:
        addNote()

    elif 'remove' in msg and 'note' in msg:
        remNote()

    elif 'create' in msg and 'plan' in msg:
        createWeekPlan()

    elif 'wake' in msg:
        askSleep('wake', msg)

    elif 'sleep' in msg:
        askSleep('sleep', msg)

    elif '?' in msg:
        sendMessage('How may I assist you, sir?')

def changeEpochToDT(epoch):
    if epoch == NO_TIME:
        return ' '
    time = str(datetime.datetime.fromtimestamp(epoch))
    return time

def getAgenda():
    file = open('todo.txt', 'r')
    agenda = file.readlines()

    i = 0

    if not agenda:
        sendMessage('No upcoming tasks, sir')

    for line in agenda :
        i += 1
        rem = line[:-13] + ' [' + changeEpochToDT(int(line[-13:-3])) + ']'
        sendMessage(str(i) + '. ' + rem)
    
def askImdb(msg):
    msg = msg.lower()

    if ('ask imdb ' in msg):
        msg.replace('ask imdb ', '')

    answer = subprocess.check_output(['python3', 'Modules/IMDB.py', msg])
    answer = getStrFromList(answer)
    
    string = 'Title: ' + answer[0] + '\nRating: ' + str(answer[1]) + '\nRuntime: ' + answer[2] + ' minutes' + '\nRelease Date: ' + answer[3] + '\nCertification: ' + answer[4]

    sendMessage(string)

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
        
    try:
        answer = subprocess.check_output(['python3', 'Modules/Wikipedia.py', msg, '5'])
    except Exception as e:
        answer = str(e)

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

    m = ''

    for i in msg:
        m = m + i
        url = url + i

    chatAction('typing')

    answer = subprocess.check_output(['python3', 'Modules/Google.py', m])
    answer = getStrFromList(answer)

    draft = '' 

    for line in answer:
        draft = draft + '\n' +  line

    sendMessage(url + '\n' )
    sendMessage(draft)
    
def askReddit(msg):
    msg = msg.lower()

    if 'ask reddit' in msg:
        msg = msg.replace('ask reddit', '')

    chatAction('typing')
    if 'joke' in msg:
        sub = 'Jokes'
    elif 'fact' in msg:
        sub = 'facts'
    elif 'news' in msg:
        sub = 'news'
    elif 'shower' in msg:
        sub = 'Showerthoughts'
    elif 'quote' in msg:
        sub = 'quotes'
    else:
        if ' ' in msg:
            msg = msg.replace (' ', '')
        sub = msg
    
    count = 5
    lst = re.findall('\d+', msg )
    if lst:
        if (lst[0] in sub):
            sub = sub.replace(lst[0], '')
        count = int(lst[0])
    elif ' a ' in msg:
        count = 1

    posts = subprocess.check_output(['python3', 'Modules/Reddit.py', sub, str(count)])
    posts = getStrFromList(posts)

    for post in posts:
        sendMessage(post[0] + '\n - \n' + post[1])

def askPi(msg):
    if 'temp' in msg:
        temp = subprocess.check_output(['bash', 'temp.sh'])
        temp = str(temp, 'utf-8')
        print(temp)
        sendMessage(temp)

    elif 'shell' in msg:
        msg = msg.replace('ask pi shell ', '')
        msg = msg.replace('shell ', '')

        if ('rm ' in msg):
            sendMessage ('Sorry Dave, I can\'t do that.')
            return 

        msg = msg.split()
        print(msg)
        out = subprocess.check_output(msg)
        print('Done')
        print(out)
        out = str(out, 'utf-8')

        # TODO remove URL links

        if out:
            sendMessage(out)
        else:
            sendMessage('Done!')

def getModule(msg):
    modules = ['reddit', 'google', 'wikipedia', 'wiki', 'alfred', 'wolfram', 'imdb', 'pi', 'comic', 'release']
    
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
    elif module == 'imdb':
        askImdb(msg)
    elif module == 'pi':
        askPi(msg)
    elif module == 'comic':
        askComic(msg)
    elif module == 'release':
        askReleases(msg)

def handle(msg):
    global chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    music_formats = ['.mp3', '.wav', '.wma', '.flac', '.3ga', '.m4a', '.aac', '.ogg']

    if (content_type == 'text'):
        HandleText(msg['text'])

    if (content_type == 'voice'):
        playAudio(msg)

    if (content_type == 'photo'):
        pass

    if (content_type == 'document'):
        if '.torrent' in msg['document']['file_name']:
            openFile(msg)

        if '.py' in msg['document']['file_name']:
            openFile(msg, pre='python3')

        else:
            for format in music_formats:
                if format in msg['document']['file_name']:
                    openFile(msg)
        
def getNextReminder():
    file = open('todo.txt', 'r')
    agenda = file.readlines()
    if not agenda:
        return []

    i = 0
    min = NO_TIME
    min_i = 0

    for line in agenda :
        i += 1
        epoch = int(line[-13:-3])
        if (NO_TIME == epoch):
            continue
        elif (epoch) < min:
            min = epoch
            min_i = i
            
    msg = {'time': min, 'message': agenda[min_i-1][:-13], 'index':min_i }
    return msg

def remove(index):
    subprocess.Popen(['python3', 'Modules/Todo.py', str(index), '0'])
    return 

def handleEvents():
    now = time.time()
    msg = getNextReminder()
    if not msg or msg['time'] == 9999999999:
        return 

    if msg['time'] < now:
        sendMessage(msg['message'])
        remove(msg['index'])

def main(): 
    global bot

    bot = telepot.Bot('232702502:AAFEUh-lDo1vb641bOJ_fJ2ar-LsVM0zeO4')
    bot.message_loop(handle)

    while True:
        time.sleep(10)
        handleEvents()
        
main()
