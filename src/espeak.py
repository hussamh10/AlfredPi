from subprocess import call

def speak(string):
    call(['espeak', string])


