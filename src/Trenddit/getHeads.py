from Trenddit import redditHandler as reddit
import time 

def main():
    while(True):
        print(reddit.getHeadlines())
        print("next")
        time.sleep(5)

main()
