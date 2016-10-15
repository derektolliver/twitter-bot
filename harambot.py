from enum import Enum
import tweepy
import twitter_info

class tweet_action(Enum):
    retweet = 1
    quote = 2
    tweet = 3

# Set authroization information
auth = tweepy.OAuthHandler(twitter_info.T['consumer_key'], twitter_info.T['consumer_secret'])
auth.set_access_token(twitter_info.T['access_token'], twitter_info.T['access_secret'])
api = tweepy.API(auth)
# api.update_status('Hope this works from heaven #immortality')

run_trainer()

with open("tweet_data.txt", "w") as data:
    for tweet in tweepy.Cursor(api.search, q='harambe', count=10000).items():
        data.write(tweet.text + "\n")
