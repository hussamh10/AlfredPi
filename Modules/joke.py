import random
import pprint
import praw
import sys

def main():

    count = int(sys.argv[1])
    user = praw.Reddit(user_agent = 'alfred')

    jokes = user.get_subreddit('jokes').get_hot(limit=20)
    jk_list = []

    r = random.sample(range(0, 19), count)
    
    i = 0
    for joke in jokes :

        if i in r:
            jk_list.append([str(joke.title), str(joke.selftext)])
        i += 1
    
    print (str(jk_list))
main()


