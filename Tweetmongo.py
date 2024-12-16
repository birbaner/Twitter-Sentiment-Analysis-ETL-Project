from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener
import json
import logging
import pymongo
import config
import time

# Connect to MongoDB
client = pymongo.MongoClient('localhost', 270**)  # Connect to localhost and port 270**
db = client.TweetDB  # Use the database named TweetDB
collection = db.TweetCollection  # Use the collection named TweetCollection

# Twitter Authentication
auth = OAuthHandler(config.CONSUMER_API_KEY, config.CONSUMER_API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True)
user = api.me()
logging.critical("Connection established with user: " + user.name)

# Function for streaming tweets
class TwitterListener(StreamListener):
    def __init__(self, limit, callback):
        self.limit = limit
        self.counter = 0
        self.callback = callback

    def on_error(self, status):
        if status == 420:
            print(status)
            return False

    def get_tweet_dict(self, t):
        if 'extended_tweet' in t:
            text = t['extended_tweet']['full_text']
        else:
            text = t['text']

        tweet = {
            'username': t['user']['screen_name'],
            'text': text,
            'followers_count': t['user']['followers_count'],
            'location': t['user']['location'],
            'description': t['user']['description']
        }

        return tweet

    def on_data(self, data):
        t = json.loads(data)
        tweet = self.get_tweet_dict(t)
        self.callback(tweet)
        self.counter += 1
        if self.counter == self.limit:
            return False

def stream_tweets(limit, callback):
    stream_listener = TwitterListener(limit, callback)
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=['OnThisDay'], follow=['2278940227'], languages=['en'])

def warning_log(tweet):
    logging.critical('\n\nTWEET: ' + tweet['username'] + ' just tweeted: ' + tweet['text'])
    collection.insert_one(tweet)

# Driver function
if __name__ == '__main__':
    while True:
        stream_tweets(5, warning_log)
        time.sleep(30)
