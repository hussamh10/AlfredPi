from subprocess import call

def speak(string):
    print("EXPEAIKING..")
    if ('say' == string.split()[0]):
        string = string.replace('say', '')
    call(['espeak', string])
