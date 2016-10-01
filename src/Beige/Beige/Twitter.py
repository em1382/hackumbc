#Author: Ellis Madagan

import tweepy

class Twitter(object):
    """Class used for communication with Twitter via Tweepy"""
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_secret = ""
    api = None
    listener = None
    stream = None

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

        self.connect()

    def connect(self):
        print("Attempting to contact Twitter API...")
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(auth)
        print("Connection Succeeded.")

    def get_public_tweets(self):
        tweets = []
        if self.api is None:
            return "No API connected, aborting."

        class MyStreamListener(tweepy.StreamListener, stream):
            def __init__(self, twitter):
                self.twitter = twitter
#penus
            def on_status(self, status):
                tweets.append(status.text.encode("utf-8"))
                if len(tweets) > 100:
                    self.twitter.stream.disconnect()
                    
                    
        self.listener = MyStreamListener()
        self.stream = tweepy.Stream(auth=self.api.auth, listener=MyStreamListener())
        self.stream.sample()
        return tweets

        
        

    
    