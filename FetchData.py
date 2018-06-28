#This is the Core Module of the project
#==== == === ==== ====== == === =======

import tweepy
import SubFunctions

#to get the user's tweets and returns the URL
def get_tweets(username):
    api = SubFunctions.get_connection()
    tweets = api.user_timeline(screen_name=username, count=20)
    URL = SubFunctions.get_URL(tweets)
    return URL

print("Connecting to Twitter...")
api = SubFunctions.get_connection()
URL = []
user = api.get_user('') #please enter your twitter username

print("Fetching information from your account...\nPlease wait, it may take a while -\n")

#extracts the friends feeds and shares
#items(2)(because it extracts less data so that output is tested), you can change it to items() to access every share(takes long time)
for friend in tweepy.Cursor(api.friends).items(2):
    URL = URL + get_tweets(friend.screen_name)

print("After fetching data from your twitter account -\n", URL)
