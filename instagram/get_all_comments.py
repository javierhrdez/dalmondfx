#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
from datetime import datetime
import requests
import pandas as pd
from pandas.io.json import json_normalize
import json

url = "https://www.instagram.com/p/BxLM31vhtxh/"

def get_media_id(url):
    req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
    media_id = req.json()['media_id']
    return media_id

# stop conditions, the script will end when first of them will be true
count = 10
username = "xavihernandezc"
password = "x9305913k"


# se debe quitar de instagram autentificación por dos factores, o de lo contrario debe investigarse como realizar el login
API = InstagramAPI(username, password)
API.login()
#API.getUsernameInfo()
has_more_comments = True
max_id = ''
comments = []



instagram = pd.DataFrame()
media_id  = get_media_id(url)
while has_more_comments:
    _ = API.getMediaComments(media_id, max_id=max_id)
    # comments' page come from older to newer, lets preserve desc order in full list
    for c in reversed(API.LastJson['comments']):
        print(c)
        datos = json_normalize(c)
        instagram = instagram.append(datos , ignore_index=True)

    has_more_comments = API.LastJson.get('has_more_comments', False)
    # evaluate stop conditions
    if count and len(comments) >= count:
        comments = comments[:count]
        # stop loop
        has_more_comments = False
        print("stopped by count")
    # next page
    if has_more_comments:
        max_id = API.LastJson.get('next_max_id', '')
        time.sleep(2)

print(instagram.head())
instagram.to_csv('instagram.csv')