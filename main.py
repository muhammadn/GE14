#!/usr/bin/env python
import facebook #import facebook-sdk
import os
import requests

graph = facebook.GraphAPI(access_token=os.environ['FB_TOKEN'], version='2.6') 
posts = graph.get_object('TunDrMahathir/posts')

p = 0
while True:
    p += 1
    if p >= 100:
        break
    for post in posts['data']:
        comments = graph.get_object(post['id'] + '/comments')
        for comment in comments['data']:
          print comment['message']
    posts = requests.get(posts['paging']['next']).json()
    for post in posts['data']:
        try:
            comments = graph.get_object(post['id'] + '/comments')
            c = 0
            while True:
                c += 1
                if c >= 1000:
                  break
                for comment in comments['data']:
                    print comment['message']
                if next in comments:
                    comments = requests.get(comments['paging']['next']).json()
                else:
                    continue
        except requests.ConnectionError:
            continue
