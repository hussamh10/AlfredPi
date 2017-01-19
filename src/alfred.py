import time
import telepot
from bot import Bot

key = '232702502:AAFEUh-lDo1vb641bOJ_fJ2ar-LsVM0zeO4'
telegram = telepot.Bot(key)
alfred = Bot(telegram)

def handle(msg):
    alfred.handle(msg)

def main():
    telegram.message_loop(handle)
    while(True):
        time.sleep(1)

main()
