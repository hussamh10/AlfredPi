import subprocess

def getLyrics(title):
    out = subprocess.check_output(['C:\\Python27\\python.exe', 'Lyrics_27.py', title])
    out = str(out, 'ascii')
    print(out)
    return out
