import csv
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import tweepy
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_key = config.access_key
access_secret = config.access_secret

def download_tweets():
    username = "elonmusk"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    num_tweets = 100

    tweets = api.user_timeline(screen_name = username, count = num_tweets)

    my_tweets = []

    for tweet in tweets:
        my_tweets.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])
        # write it out to a csv
        with open("{0}_tweets.csv".format(username), 'w+') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(my_tweets)

if __name__ == '__main__':
    download_tweets()
