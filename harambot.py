from enum import Enum
import tweepy
from trainer import Trainer
import twitter_info
import random


class tweet_action(Enum):
    retweet = 1
    quote = 2
    tweet = 3

# Set authroization information
auth = tweepy.OAuthHandler(twitter_info.T['consumer_key'],
                           twitter_info.T['consumer_secret'])
auth.set_access_token(twitter_info.T['access_token'],
                      twitter_info.T['access_secret'])
api = tweepy.API(auth)

t = Trainer(api)
action = random.randint(1, 4)
t.run_trainer(action)

if action == tweet_action.retweet:
    api.retweet(t.id)
elif action == tweet_action.quote:
    api.update_status(t.tweet + " " + t.url)
else:
    print('TWEET:')
    print(t.tweet)
    api.update_status(t.tweet)
