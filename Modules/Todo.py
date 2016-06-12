import sys

def main():

    msg = sys.argv[1]
    flag = sys.argv[2]

    print (flag)

    if flag == '1':
        print (msg + "Writing")
        file = open('todo.txt', 'a')
        print('ok')
        file.write(msg + '\n')
        file.close()
        return 

    if flag == '0':

        file = open('todo.txt', 'r')
        cont = file.readlines()

        file.close()

        file = open('todo.txt', 'w')
        i = 1
        
        for line in cont:
            if i == int(msg):
                i += 1
                continue
            else:
                i += 1
                file.write(line)

main()
