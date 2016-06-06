import wolframalpha
import sys
import pprint

client = wolframalpha.Client('PGQ3TL-EXWG2EA68R')

arg_count = len(sys.argv) - 1
string = ''

for i in range(0, arg_count):
    string = string + ' ' + sys.argv[i+1]
string = string[1:]

print (string)

res = client.query(string)

for pod in res.pods:
	print(pod.text)
	


