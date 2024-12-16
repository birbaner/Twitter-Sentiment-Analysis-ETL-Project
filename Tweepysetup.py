import tweepy

# Your credentials
API_KEY = ''
API_KEY_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def authenticate():
    # OAuth 1.0 Authentication
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth

if __name__ == '__main__':
    auth = authenticate()
    api = tweepy.API(auth)

    # Verify the authentication
    try:
        api.verify_credentials()
        print("Authentication Successful!")
    except Exception as e:
        print(f"Authentication failed: {e}")
