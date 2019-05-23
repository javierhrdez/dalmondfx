"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests
from pprint import pprint
import pandas as pd
from pandas.io.json import json_normalize




def some_action(df,post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print('--------------------------------')
    pprint(post)
    datos = json_normalize(post)
    df = df.append(datos , ignore_index=True)
    return df
    #print(post.get('created_time'))
    #print(post.get('message'))
    #if post['message']:
    #    print(post['message'])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Look at Bill Gates's profile for this example by using his Facebook id.
#user = "me/posts"
user  = "me"

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
#profile = graph.get_object(id = "me/posts", field="permalink_url,created_time,type,name,id,comments.limit(0).summary(true),shares,likes.limit(0).summary(true),reactions.limit(0).summary(true)")
#https://graph.facebook.com/v3.3/me/posts/?fields=message,link,permalink_url,created_time,type,name,id,comments.limit(0).summary(true),shares,likes.limit(0).summary(true),reactions.limit(0).summary(true)&access_token=EAAfkjHpDd3QBAOxfWB7QBrWD6Rd252vq9RGfQNnOGD9

print(profile)
posts = graph.get_connections(profile["id"], "posts")
#print(posts)
# Wrap this block in a while loop so we can keep paginating requests until
# finished.


fb = pd.DataFrame()
while True:
    try:
#        # Perform some action on each post in the collection we receive from
#        # Facebook.
        for post in posts["data"]:
            fb = some_action(fb,post=post)
        #[some_action(fb,post=post) for post in posts["data"]]
#        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts["paging"]["next"]).json()
    except KeyError:
#        # When there are no more pages (['paging']['next']), break from the
#        # loop and end the script.
        break

print(fb.head())
fb.to_csv('fb.csv')