import tweepy
from tweepy import StreamingClient, StreamRule

# Replace 'YOUR_BEARER_TOKEN' with your actual Bearer Token
bearer_token = ''

# Custom StreamingClient class
class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")

# Instantiate the StreamingClient with the Bearer Token
stream = TweetPrinterV2(bearer_token)

# Add a rule for streaming specific tweets
rule = StreamRule(value="OnThisDay")
stream.add_rules(rule)

# Start streaming
stream.filter()
