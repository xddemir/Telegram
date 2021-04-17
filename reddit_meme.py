import praw
import info
import random
class reddit():
    def __init__(self,password,username):
        self.username=username
        self.password=password
        self.reddit = praw.Reddit(client_id='',
                            client_secret='',
                            password=self.password,
                            username=self.username,user_agent='penguinz01')
    def get_meme(self):
        self.reddit.read_only=True
        meme_lst=[]
        subreddit=self.reddit.subreddit('meme').hot(limit=10)
        for submisson in subreddit:
            if str(submisson.url).endswith(".jpg"):
                meme_lst.append(submisson.url)
        _=random.randint(0,9)
        return meme_lst[_]

    def get_gif(self): # it will improve more......
        a=[]
        self.reddit.read_only=True
        subgif=self.reddit.subreddit('gif').hot(limit=100)
        gif_lst=[i.url for i in subgif]
        for i in gif_lst:
            if i.endswith(".gif")==True:
                a.append(i)
        _rand=random.randint(0,len(a))
        return a[_rand]



