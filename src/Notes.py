import sys

def addNote(msg):
    msg = msg.replace('\n', '$')

    file = open('notes.txt', 'a')
    file.write(msg + '\n')
    file.close()

def getNotes():
    file = open('notes.txt', 'r')
    notes = file.read()
    notes = notes.replace('$', '\n')
    file.close()
    return notes

def removeNote(index):
    file = open('notes.txt', 'r')
    notes = file.readlines()
    file.close()
    file = open('notes.txt', 'w')
    i = 1

    for line in notes:
        if i in index:
            i += 1
            continue
        else:
            i += 1
            file.write(line)
