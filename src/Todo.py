import sys

def addTodo(msg):
    file = open('todo.txt', 'a')
    file.write(msg + '\n')
    file.close()

def getTodos():
    file = open('todo.txt', 'r')
    cont = file.read()
    return cont

def removeTodo(index)
    file = open('todo.txt', 'r')
    cont = file.readlines()
    file.close()

    file = open('todo.txt', 'w')
    i = 1

    for line in cont:
        if i == index:
            i += 1
        else:
            i += 1
            file.write(line)
