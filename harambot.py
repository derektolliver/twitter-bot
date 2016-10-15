import tweepy
import twitter_info


auth = tweepy.OAuthHandler(twitter_info.T['consumer_key'], twitter_info.T['consumer_secret'])

auth.set_access_token(twitter_info.T['access_token'], twitter_info.T['access_secret'])

api = tweepy.API(auth)
# api.update_status('Hope this works from heaven #immortality')

for tweet in tweepy.Cursor(api.search, q='harambe').items():
    print(tweet.text)
    print('#############################################')
