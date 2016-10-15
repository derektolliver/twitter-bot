from harambot import tweet_action
from collections import defaultdict
import harambot
import tweepy

class trainer(object):
    def __init__(self, api):
        self.api = api
        self.url = None
        self.tweet = None

    def run_trainer(action):
        quote_size = 0
        if action != tweet_action.tweet:
            self.url = self.find_tweet()
            quote_size = len(self.url)
        if action != tweet_action.retweet:
            self.tweet = self.create_tweet(quote_size)

    def find_tweet():
        return tweepy.Cursor(self.api.search, q='harambe', count=1)[0]

    def create_tweet(quote_size):
        num_chars = random.randint(20, 140 - quote_size)
        chains = markov_chains()
        choice = random.choice(chains.keys())
        while num_chars - len(choice) > 0:
            result += choice + " "
            num_chars -= len(choice) + 1
            choice = find_next_choice(chains[choice])
        if len(result) > 140:
            throw ValueError("Result is too long")
        return result

    def find_next_choice(options):
        pick = random.uniform(0, sum(options.values()))
        current = 0
        for o in options.keys():
            current += options[o]
            if current >= pick:
                return o
        return random.choice(options.keys())

    def markov_chains():
        result = defaultdict(lambda : defaultdict(int))
        for tweet in tweepy.Cursor(self.api.search, q="harambe", count=10000):
            words = [elem for elem in tweet.split()]
            for index in range(0, len(words) - 1):
                result[words[index]][words[index + 1]] += 1
        return result
