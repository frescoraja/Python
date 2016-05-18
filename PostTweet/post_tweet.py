import tweepy
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_key = config.access_key
access_secret = config.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

# api.update_status(status="Using PYTHON and the tweepy library to hit up the Twitter API.. TWEET TWEET. !")
api.update_with_media("POTUS_tweets.png","President Obama's word cloud from his latest 200 tweets..")
