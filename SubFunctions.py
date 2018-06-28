#All the passwords and sub methods are implemented here
#=== === ========= === === ======= === =========== ====

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

import re
import tweepy

#to extract URL in the tweets
def get_URL(tweets):
    URL = []
    for tweet in tweets:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.text)
        for url in urls:
            URL.append(url)
    return URL

#to get connection
def get_connection():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth)