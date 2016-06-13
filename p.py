import telepot

bot = 0
chat_id = 0

def handle(msg):
    
    global chat_id


    print('adsf')
    
    content_type, chat_type, chat_id = telepot.glance(msg)

    print(chat_id)

    bot.sendMessage(chat_id, 'http://www4b.wolframalpha.com/Calculate/MSP/MSP37121g2e5c9c2bg06d1g00002c9aa81749f1hdb1?MSPStoreType=image/gif&s=37')
    bot.sendMessage(chat_id, 'Hello')
    bot.sendPhoto(chat_id, open('l.jpg', 'rb'))

    print('sent')


 

def main(): 

    global bot

    bot = telepot.Bot('232702502:AAFEUh-lDo1vb641bOJ_fJ2ar-LsVM0zeO4')

    bot.message_loop(handle)

    while True:
        pass
    

main()
