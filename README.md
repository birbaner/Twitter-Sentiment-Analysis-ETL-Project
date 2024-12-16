# Twitter-Sentiment-Analysis-ETL-Project

**Overview**

This project demonstrates the process of collecting realtime tweets using the Twitter API, storing them in MongoDB, analyzing their sentiment, and saving the processed data into a PostgreSQL database. The pipeline is built using Python and leverages libraries like Tweepy, VADER SentimentIntensityAnalyzer, and TextBlob. The goal of this project is to create a database of tweets that use the hashtag #OnThisDay along with their sentiment score.

**The Docker-Compose pipeline includes four steps (containters):**

**Tweet Collection**
1.Collects live tweets using the Twitter API and the tweepy library.
2.Streams tweets containing the hashtag #OnThisDay.
3.Extracts tweet text and user handles.

**Storing Tweets in MongoDB**

1.Stores collected tweets in a MongoDB database.
2.Utilizes MongoDB’s JSON-like document structure for efficient storage of tweet data.

**ETL Process**
1.Extract: Fetches stored tweets from MongoDB.
2.Transform: Analyzes tweet sentiment using the VADER library and computes sentiment scores.
3.Load: Saves tweets along with their sentiment scores into a PostgreSQL database.

**PostgreSQL Storage**
Saves tweets into a table with fields for text, sentiment scores, and other metadata.

**Installation**
Prerequisites
Python (version 3.8 or higher)
MongoDB
PostgreSQL
Twitter Developer Account with API credentials

**Libraries**
Install the required Python libraries using pip:
pip install tweepy pymongo sqlalchemy psycopg2-binary vaderSentiment textblob

**Setup**
**Twitter API**
1.Create an app on the Twitter Developer Portal.
2.Obtain your API key, API secret key, Access token, and Access token secret.
3.Add these credentials to a config.py file:
CONSUMER_API_KEY = 'your_api_key'
CONSUMER_API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

**MongoDB Setup**
1.Create a MongoDB account at MongoDB Compass.
2.Set up a cluster and create a database named TweetDB with a collection named TweetCollection.
3.Allow access to your IP and connect to the database.
4.Update the MongoDB connection string in the Python script.

**PostgreSQL Setup**
1.Install PostgreSQL on your system(Ubuntu/Linux).
2.Create a database named twitter:
createdb twitter
3.Create a table for storing tweets:
CREATE TABLE tweets (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    text TEXT,
    sia_score NUMERIC(4,3),
    blob_polarity NUMERIC(4,3),
    blob_subjectivity NUMERIC(4,3)
);

**Workflow**

**1. Collecting Tweets**
Use the tweepy library to stream live tweets containing the hashtag #OnThisDay.
Save the tweet text, username, and additional metadata.

**2. Storing Tweets in MongoDB**
Store the collected tweets in a MongoDB collection named TweetCollection within the TweetDB database.

**3. Performing ETL Job**

**Extract**
Retrieve tweets from MongoDB using the pymongo library.

**Transform**
Use the VADER Sentiment Analysis library to compute sentiment scores.
Use TextBlob for additional polarity and subjectivity analysis.

**Load**
Save the transformed tweets into the PostgreSQL database using the sqlalchemy library.





