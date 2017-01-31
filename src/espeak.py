from subprocess import call

def speak(string):
    if ('say' == string.split()[0]):
        string = string.replace('say', '')
    call(['espeak', string])


