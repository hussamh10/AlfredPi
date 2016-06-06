import sys

def main():

    msg = sys.argv[1]

    file = open('todo.txt', 'w')
    file.write(msg)

main()
