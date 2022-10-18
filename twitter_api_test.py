from os import access
import tweepy
import configparser
import pandas as pd
from tweepy import OAuthHandler
import time
import sys

tweets=[];
def writeToTxt(tweets):
    columns = ['Time', 'User','ID', 'Tweet']
    data = []
    for tweet in tweets:
        print(tweet)
        data.append([tweet.created_at, tweet.user.screen_name,tweet.id, tweet.text])

    df = pd.DataFrame(data, columns=columns)

    # 現在の日時を取得
    now = time.localtime()
    date = time.strftime('%Y%m%d_%H%M%S', now)

    #ファイル名設定
    file = 'tweets_'
    extension = '.csv'
    name = file + date + extension

    df.to_csv(name)

def main():
    config = configparser.ConfigParser()
    #設定ファイル読み込む
    config.read('config.ini')

    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']

    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    auth = OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token,access_token_secret)

    #制限になったら、まちます
    api = tweepy.API(auth, wait_on_rate_limit=True)    
    #制限になったら、ファイル保存してプログラムを止める
    #api = tweepy.API(auth, wait_on_rate_limit=False)    

#   キーワード設定

    search_words = ["コロナ  min_faves:5 since:2022-10-11 until:2022-10-18"]

    tweets = tweepy.Cursor(api.search_tweets,q=search_words, result_type='recent',
                        #どこからツイットを得るか
                    geocode="35.68046,139.68875,3000km",
                    #最大のIDから取ってくる
                    #max_id=1581934317323763713,
                    ).items(10000) #何件までを得るか？
    writeToTxt(tweets)
#print(tweets)

# columns = ['Time', 'User','ID', 'Tweet']
# data = []
# for tweet in tweets:
#     print(tweet)
#     data.append([tweet.created_at, tweet.user.screen_name,tweet.id, tweet.text])

# df = pd.DataFrame(data, columns=columns)

# # 現在の日時を取得
# now = time.localtime()
# date = time.strftime('%Y%m%d_%H%M%S', now)

# #ファイル名設定
# file = 'tweets_'
# extension = '.csv'
# name = file + date + extension

# df.to_csv(name)

if __name__ == '__main__':
    main()
    # try:
    #     main()
    # except KeyboardInterrupt:
    #     print("Keyboard Interrupted by user!")
    #     writeToTxt(tweets)
    #     sys.exit()
    # except:
    #     print("Rate limit reach!")
    #     writeToTxt(tweets)
    #     sys.exit()


# for tweet in tweets:
#     print("created_at: {}\nuser: {}\ntweet text: {}\ngeo_location: {}".
#             format(tweet.created_at, tweet.user.screen_name, tweet.text, tweet.user.location))
#     print("\n")
## tweet.user.location will give you the general location of the user and not the particular location for the tweet itself, as it turns out, most of the users do not share the exact location of the tweet
