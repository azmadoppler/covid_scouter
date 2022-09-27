from os import access
import tweepy
import configparser
import pandas as pd
from tweepy import OAuthHandler

#read config

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth, wait_on_rate_limit=True)    # set wait_on_rate_limit =True; as twitter may block you from querying if it finds you exceeding some limits



search_words = ["コロナ until:2022-09-10 since:2022-09-01"]



tweets = tweepy.Cursor(api.search_tweets,q=search_words,
                       #geocode="35.68046,139.68875,3000km",
                       ).items(10)
## the geocode is for India; format for geocode="lattitude,longitude,radius"
## radius should be in miles or km

print(tweets)

columns = ['Time', 'User', 'Tweet']
data = []
for tweet in tweets:
    print(tweet)
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)



df.to_csv('tweets2.csv')




# for tweet in tweets:
#     print("created_at: {}\nuser: {}\ntweet text: {}\ngeo_location: {}".
#             format(tweet.created_at, tweet.user.screen_name, tweet.text, tweet.user.location))
#     print("\n")
## tweet.user.location will give you the general location of the user and not the particular location for the tweet itself, as it turns out, most of the users do not share the exact location of the tweet