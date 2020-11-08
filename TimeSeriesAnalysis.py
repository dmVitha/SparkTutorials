import tweepy as tw
import pandas as pd
import dateutil.parser
import  datetime

import re
import string
import csv
import nltk


consumer_key = 'lUCGJlG8p7T18KN1PGivrh39m'
consumer_secret = '2DVI0wekSaxHpROrKVIJCIkE3BNwcoSITzv48z6Xzy5CZOSOFo'
access_token = '1074077006424207360-1SDPM8jppHeCTsgylOeAgRfE9n4A3D'
access_secret = 'SEcF6ZBgbX8w3jdrz6SiYcYA6SQWNnKTE6QXSwjmFU67J'


def get_tweets(search_words,date_until):
    print("returning tweets")
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tw.API(auth,wait_on_rate_limit=True)
    tweets = tw.Cursor(api.search, q=search_words, lang="si",until=date_until).items()
    tweets = [[tweet.created_at, tweet.text] for tweet in tweets]
    # print(list(tweets))

    df = pd.DataFrame(tweets, columns=['Created At', 'Text'])
    df['Created At'] = pd.to_datetime(df['Created At'])
    # df['Text']=df['Text'].astype('str')

    # df.to_csv('sinhala_tweets.csv',encoding="utf-8")
    fields=['Created At','Text']
    with open("sinhala_tweets.csv", 'a+', newline='',encoding="utf-8") as csvFile:
        df.to_csv(csvFile)
    csvFile.close()

# Driver code
if __name__ == '__main__':
    get_tweets("COVID-19 ", "2020-11-06")