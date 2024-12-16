import pymongo
from sqlalchemy import create_engine
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import logging
import random

# Sleep to ensure services are up
time.sleep(5)

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:****@localhost:5432/twitter')  # Replace 'your_password' with your PostgreSQL password

# Create the table if it doesn't exist
create_query = """
CREATE TABLE IF NOT EXISTS tweets (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    text TEXT,
    sia_score NUMERIC(4,3),
    blob_polarity NUMERIC(4,3),
    blob_subjectivity NUMERIC(4,3)
);
"""
engine.execute(create_query)

# Connect to MongoDB
client = pymongo.MongoClient(host='localhost', port=270**)
db = client.TweetDB
collection = db.TweetCollection

# Extract tweets from MongoDB
def extract_tweets():
    tweets = list(collection.find())  # Fetch all documents from MongoDB
    if tweets:
        t = random.choice(tweets)  # Select a random tweet
        logging.critical(f"Random tweet: {t['text']}")
        return t
    return None

# Perform sentiment analysis
def transform_tweets(tweet):
    tweet_text = tweet['text'].replace("'", "''")  # Escape single quotes for SQL
    sia = SentimentIntensityAnalyzer()
    sia_score = sia.polarity_scores(tweet_text)['compound']
    blob = TextBlob(tweet_text).sentiment
    return sia_score, blob.polarity, blob.subjectivity

# Load data into PostgreSQL
def load_tweets(tweet, sia_score, blob_polarity, blob_subjectivity):
    insert_query = f"""
    INSERT INTO tweets (username, text, sia_score, blob_polarity, blob_subjectivity)
    VALUES ('{tweet["username"]}', '{tweet["text"].replace("'", "''")}', {sia_score}, {blob_polarity}, {blob_subjectivity});
    """
    engine.execute(insert_query)
    logging.critical(f"Tweet by {tweet['username']} loaded into PostgreSQL.")

# ETL Job
logging.critical("Starting ETL job")
while True:
    tweet = extract_tweets()
    if tweet:
        sia_score, blob_polarity, blob_subjectivity = transform_tweets(tweet)
        load_tweets(tweet, sia_score, blob_polarity, blob_subjectivity)
    time.sleep(10)
