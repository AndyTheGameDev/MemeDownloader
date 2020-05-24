import praw
import urllib

reddit = praw.Reddit(client_id='oSLdsCucOTrlmg', client_secret='EJv9K1W-PbsgLQNIvauCeaSLGW4',  user_agent='Meme Collector by /u/and249')

sub = input("Enter the name of the subreddit : ")
lim = int(input("Enter the number of memes you wanna download : "))
title = []
urls = []
i = 1
bad_chars = [' \ ', '/', ':', '*', '?', '"', '<', '>', '|']
ttl = ''

# Getting the memes

while i <= lim:
    submission = reddit.subreddit(sub).random()
    url = submission.url

    if url not in urls:
        if url.endswith('jpg') or url.endswith('jpeg') or url.endswith('png'):
            urls.append(url)
            title.append(submission.title)
            i += 1
    else:
        continue

# Getting rid of the bad chars
for i in range(len(title)):
    for j in bad_chars:
        title[i] = title[i].replace(j, '_')

# Downloading the good stuffs
for i in range(len(urls)):
    urllib.request.urlretrieve(urls[i], f"{title[i]}.jpg")

print("The memes have been successfully downloaded! Have fun now :D")
