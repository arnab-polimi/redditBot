#!/usr/bin/env python
# coding: utf-8

# In[13]:


#######
#praw shit#
# Arnab Mondal #
#######


# In[14]:


import praw
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()



reddit = praw.Reddit(client_id = '-KRP353eA27Tq3z-HVqtVA' ,
                    client_secret = 'XcXzena1lToC-aLmdzCpmbgGKp0a0w',
                    username = 'signalproc',
                    password = 'Amondal97##',
                    user_agent = 'reddBot',)


# In[15]:


# to verify me
print(reddit.user.me())


# In[9]:


'''
This bot is supposed to ask you for your favorite subreddits and then give you the hot posts according to the keywords you
searched for, super cool isn't it?

'''
n_subs = input('How many subreddits do you want to put ? \n ')
n_keywords = input('Number of keywords \n')
keywords = []
subs = []


for s in range(int(n_subs)):
    sub = input(' Subreddits: ')
    subs.append(sub)
for k in range(int(n_keywords)):
    keyword = input(' Keywords: ')
    keywords.append(keyword)
    
print('So your subreddits chosen are : \n',subs)
print('And the keywords you are looking for are \n:',keywords)

print(20*'*')

for sub in subs:
    subreddit = reddit.subreddit(sub)
    hot_topics = subreddit.search(keywords,sort = 'upvotes',limit = 20 )
    print('-----------TITLE OF THE POST-----------')
    
   
    for submission in hot_topics:        
        if not submission.stickied:
            print('Title :{}, ups :{}, Link:{}'.format(submission.title, submission.ups, "https://www.reddit.com" + submission.permalink))
            submission.comments.replace_more(limit=0)
            comments = submission.comments.list() 
            for comment in comments:
                print('\n')
                print('---new comment---')
                print(comment.body)
                print('---end of the comment')
                print('\n')
                

            
                
        


# In[ ]:




