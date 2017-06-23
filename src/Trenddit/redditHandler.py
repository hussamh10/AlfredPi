from Trenddit import Reddit

def getHeadlines():
    sent_file = open('Trenddit\sent', 'r')
    subs = open('Trenddit\subs', 'r').read().split()

    sent = sent_file.read().split()
    sent_file.close()

    sent_file = open('Trenddit\sent', 'a')

    headlines = []

    for sub in subs:
        subreddit = Reddit.getSubreddit(sub)
        posts = Reddit.getTopPosts(subreddit)
        filtered = Reddit.filter(posts, subreddit)
        for p in filtered:
            print(p.getId())
            if p.getId() not in sent:
                print('ok')
                headlines.append(p.toString())
                sent_file.write(" " + p.getId())

    sent_file.close()
    return headlines

if __name__ == '__main__':
    getHeadlines()
