from subprocess import check_output

def scan():
    out = check_output(['bash', 'scan.sh'])

    if ('hussam' in out):
        print('hussam')
    if ('Samsung' in out):
        print('mama')

