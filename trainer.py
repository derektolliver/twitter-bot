from collections import defaultdict
import tweepy
from enum import Enum
import random


class tweet_action(Enum):
    retweet = 1
    quote = 2
    tweet = 3


class Trainer(object):
    def __init__(self, api):
        self.api = api
        self.id = None
        self.url = None
        self.tweet = None

    def run_trainer(self, action):
        url_present = False
        if action != tweet_action.tweet:
            self.find_tweet()
            url_present = True
        if action != tweet_action.retweet:
            self.tweet = self.create_tweet(url_present)

    def find_tweet(self):
        tweet = next(tweepy.Cursor(self.api.search, q='harambe', count=1).items())
        self.id = tweet.id
        self.url = "https://twitter.com/" + tweet._json['user']['screen_name'] + \
            "/status/" + str(tweet.id)

    def create_tweet(self, url_present):
        result = ""
        upper_bound = 140
        if url_present:
            upper_bound -= 24
        num_chars = random.randint(20, upper_bound)
        chains = self.markov_chains()
        keys = [elem for elem in chains.keys()]
        choice = random.choice(keys)
        while num_chars - len(choice) > 0:
            result += choice + " "
            num_chars -= len(choice) + 1
            if not chains[choice]:
                break
            choice = self.find_next_choice(chains[choice])
        if len(result) > 140:
            raise ValueError("Result is too long")
        return result[:len(result) - 1]

    def find_next_choice(self, options):
        pick = random.uniform(0, sum(options.values()))
        current = 0
        for o in options.keys():
            current += options[o]
            if current >= pick:
                return o
        keys = [elem for elem in options.keys()]
        print(options)
        print(keys)
        return random.choice(keys)

    def markov_chains(self):
        result = defaultdict(lambda: defaultdict(int))
        cursor = tweepy.Cursor(self.api.search, q="harambe").items()
        count = 0
        while count < 100:
            tweet = next(cursor)
            words = [elem for elem in tweet.text.split()]
            for index in range(0, len(words) - 1):
                result[words[index]][words[index + 1]] += 1
            count += 1
        return result

    def store_date(self):
        with open('tweet_date.txt', 'w') as data:
            cursor = tweepy.Cursor(self.api.search, q="harambe").items()
            count = 0
            while count < 100:
                tweet = next(cursor)
                data.write(tweet.text + '\n')
                count += 1

