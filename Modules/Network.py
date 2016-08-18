from subprocess import check_output
import sys
import time

def main():
    i = 0
    deep = False

    if (sys.argv[-1] == 'True'):
        deep = True

    hussam = False
    hussamPC = False
    amman = False
    ammanPC = False
    mama = False
    azmi = False
    hiba = False
    ps4 = False

    if deep :
        i = -4

    while (i < 2):
        i += 1
        out = check_output(['bash', 'Modules/network.sh'])
        out = str(out, 'utf-8')

        if ('hussam-PC' in out):
            hussamPC = True
        if ('OnePlus' in out):
            hussam = True
        if ('Amman' in out) :
            ammanPC = True
        if ("EC:1F" in out):
            amman = True
        if ('E8:61' in out):
            ps4 = True

    if ammanPC:
        print('Amman\'s Laptop')
    if amman:
        print('Amman\' S6')
    if mama:
        print('mama')
    if hussam:
        print('Hussam\'s OnePlus')
    if hussamPC:
        print('hussam\'s Laptop')
    if hiba:
        print('hiba')
    if ps4:
        print('ps4')
       
main()
