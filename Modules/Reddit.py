import random
import pprint
import praw
import sys

def reddit(sub, count):

    user = praw.Reddit(user_agent = 'alfred')

    out = user.get_subreddit(sub).get_hot(limit=20)
    list = []

    r = random.sample(range(0, 19), count)
    i = 0

    for post in out :
        if i in r:
            if 'www.reddit' in post.url:
                list.append([(post.title), (post.selftext)])
            else:
                list.append([(post.title), (post.selftext) + ' ' + (post.url)])
        i += 1
    
    try :
        print (str(list))
    except Exception as e:
        list = [['Encode ' , 'Error']]
        print (str(list))
    
def main():

    sub = sys.argv[-2]
    count = int(sys.argv[-1])

    reddit(sub, count)

main()


