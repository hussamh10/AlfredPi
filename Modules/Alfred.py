import sys
import random

def main():

    arg = sys.argv[1]

    if '1' in arg:
        r = random.randint(0, 1)
        if r == 1:
            print ('Heads')
        else:
            print ('Tails')

    if '2' in arg:
        r = random.randint(0, 2)
        if r == 1:
            print ('Rock')
        elif r == 2:
            print ('Paper')
        else:
            print ('Scissors')


main()
