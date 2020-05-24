import praw
import random
from random import shuffle
import urllib

reddit = praw.Reddit(client_id='oSLdsCucOTrlmg', client_secret='EJv9K1W-PbsgLQNIvauCeaSLGW4',  user_agent='Meme Collector by /u/and249')
sub = input("Enter the name of the subreddit you want to download images from : ")
urls = []
down = []

# Getting top 150 memes
for submission in reddit.subreddit(sub).hot(limit=150):
    url = submission.url
    if url.endswith('jpg') or url.endswith('jpeg') or url.endswith('png'):
        urls.append(url)

# Making sure that things don't repeat
shuffle(urls)
for i in range(150):
    x = random.choice(urls)
    if x not in down:
        down.append(x)
    else:
        continue

    if len(down) == 15:
        break

count = 0

# Downloading the memes
for i in range(len(down)):
    count += 1
    urllib.request.urlretrieve(down[i], f"image{count}.jpg")

print('The memes have been successfully downloaded')
