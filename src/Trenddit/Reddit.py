from Trenddit import Post
from Trenddit import Search_Google
import praw
import sys

authentication = open('authentication', 'r').readlines()
praw.reddit.read_only = True
bot = praw.Reddit(user_agent='Alfred v0.1',
                client_id='OoYLyu-_HnuIIA',
                client_secret='m2ZY_l0LBEF3h6TInLOt1tCkHaw',
                username=authentication[0][:-1],
                password=authentication[1][:-1])


def getSubreddit(r):
    return bot.subreddit(r)
    url = Search_Google.getUrl(r, 'reddit.com', 1)
    url = url.split('/')
    subreddit = url[-2]
    return bot.subreddit(subreddit)

def getTopPosts(subreddit):
    posts = []
    for post in subreddit.top('day'):
        posts.append(post)
        title = post.title
        if sys.platform == "win32":
            title = title.encode('cp65001')
        else:
            title = title.encode('utf-8')

    return posts[:5]


def filter(posts, subreddit):
    subscribers = subreddit.subscribers

    filtered = []

    for post in posts:
        id = post.permalink.split('/')
        id = id[-3]
        p = Post.Post(id, subreddit.display_name, post.title)
        if subscribers < 60000:
            if post.score > subscribers * 0.005:
                filtered.append(p)
        else:
            if post.score > subscribers * 0.003:
                filtered.append(p)

    return filtered
