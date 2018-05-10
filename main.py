#!/usr/bin/env python
import facebook #import facebook-sdk
import os
import requests
from elasticsearch import Elasticsearch

es = Elasticsearch()
graph = facebook.GraphAPI(access_token=os.environ['FB_TOKEN'], version='2.6') 
# You can change it to any other pages/facebook public profiles
posts = graph.get_object('TunDrMahathir/posts')

p = 0
while True:
    p += 1
    if p >= 100:
        break
    for post in posts['data']:
        comments = graph.get_object(post['id'] + '/comments')
        for comment in comments['data']:
            doc = {
                'message': comment['message'],
                'timestamp': comment['created_time'],
            }
            es.index(index="ge14-index", doc_type='comment', id=comment['id'], body=doc)
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
                    doc = {
                        'message': comment['message'],
                        'timestamp': comment['created_time'],
                    }
                    es.index(index="ge14-index", doc_type='comment', id=comment['id'], body=doc)
                    print comment['message']
                if next in comments:
                    comments = requests.get(comments['paging']['next']).json()
                else:
                    continue
        except requests.ConnectionError:
            continue
