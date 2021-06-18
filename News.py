# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 21:49:26 2021

@author: himan
"""

import requests
import json
import plyer
import datetime
import time
while(1):
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=caeecdaf3ecb4f3fa2aaf9665fdf3fc9')
    r = requests.get(url)
    news = r.text

    dict = json.loads(news)

    newsdict = dict['articles']

    tod = datetime.datetime.today()
    todstr = tod.strftime('%d %m %y')
    for i in newsdict:
        plyer.notification.notify(
            title = "News Notification " + todstr,
            message = "Title: " + i['title'] + '\n' +
            "URL: " + i['url'],
            timeout = 5
            )
        
    time.sleep(100)
