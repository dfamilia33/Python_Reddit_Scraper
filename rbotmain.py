# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:27:25 2018

@author: Daniel
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 19:39:06 2018

Reddit Python Bot 

Plan: Build bot that:
    1.scans subreddit
    2.find keywords ('Adidas', 'Vans', 'jeans', 'Hilfiger')
    3.stores post id to remember
    4.pms main account with link
    
    
@author: Daniel
"""

import praw
import time
import rbotemailscript
import config

#Account and password info stored in config.py
def check_id(ids):
    with open('redditids.txt', 'r') as redditidfile:
        for line in redditidfile:
            if ids in line: #TO DO sort & implement bisection search
                return True
            
    return False
                                



redditids = ['foo','bar']
count = 0

reddit = praw.Reddit(client_id = 'xPUk-TGUkfOB5Q',
                     client_secret = '1ytsajje5Qzhe0BUsnQWCmq36yo',
                     username = 'dealbot33', password= config.botpass,
                     user_agent = 'foobar')

keywords = [['Timberland','boot','boots','Boot','Boots','Hilfiger','Mason'],
            ['freshman','Freshman','Freshmen','Freshmen',]]


#Roseville is a test string


while count < 2:
    it = count % 2 #Iterates over male fashion subreddit and CS subreddit
    subreddits = [reddit.subreddit('frugalmalefashion'), reddit.subreddit('cscareerquestions')]

    hot_posts = subreddits[it].hot(limit = 12)
    
    for submission in hot_posts:
        idused = False
        if not submission.stickied:
            link = "https://www.reddit.com" + submission.permalink
            ids = str(submission)
            
            try:
                u'\u2019'.encode('ascii', 'ignore')
                title = str(submission.title)
            except UnicodeEncodeError:
                title = "UnicodeEncodeError"
                idused = check_id(ids)
                
                if idused == False:
                    rbotemailscript.email_self("Error",title,link)
                    with open('redditids.txt','a') as redditidfile:
                        redditidfile.write('\n' + ids)
                
            
            
            for brand in keywords[it]:
                if brand in title:
                    idused = check_id(ids)
                    if idused == False:
                        with open('redditids.txt','a') as redditidfile:
                            redditidfile.write('\n' + ids)
                            
                        
                        if it == 0:
                            rbotemailscript.email_self("Deal Found!",title,link)
                        elif it == 1:
                            rbotemailscript.email_self("Computer Science Discussion",title,link)
                        else:
                            pass
                            
                    else:
                        pass
    count += 1
 