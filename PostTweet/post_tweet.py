import tweepy
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_key = config.access_key
access_secret = config.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

api.update_status(status="WOOHOO TEWEETING! AGAIN!!! and what not ..")
api.update_with_media("elonmusk_tweets.png", "Elon musk's most commonly used words in last 100 tweets")
