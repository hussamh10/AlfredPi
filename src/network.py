from subprocess import check_output

def main():
    out = check_output(['bash', 'network.sh'])

    if ('OnePlus' in out):
        print('hussam')
    if ('Samsung' in out):
        print('mama')

main()

