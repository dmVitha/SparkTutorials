import tweepy as tw
import pandas as pd
import dateutil.parser
import  datetime
from pandas import DataFrame
import re
import string
import csv
import nltk


consumer_key = 'lUCGJlG8p7T18KN1PGivrh39m'
consumer_secret = '2DVI0wekSaxHpROrKVIJCIkE3BNwcoSITzv48z6Xzy5CZOSOFo'
access_token = '1074077006424207360-1SDPM8jppHeCTsgylOeAgRfE9n4A3D'
access_secret = 'SEcF6ZBgbX8w3jdrz6SiYcYA6SQWNnKTE6QXSwjmFU67J'


def get_tweets():
    print("returning tweets")
    SL_WOE_ID=23424778
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tw.API(auth,wait_on_rate_limit=True)
    # tweets = tw.Cursor(api.search, q=search_words, lang="si",until=date_until).items()
    # tweets = [[tweet.created_at, tweet.text] for tweet in tweets]


    adaDerana = api.user_timeline(screen_name="@adaderanasin",
                               count=200,
                               lang="en",
                               since=datetime.datetime(2021, 5, 1, 0, 0, 0),
                               include_rts=False,
                               tweet_mode='extended'
                               );

    cNews = api.user_timeline(screen_name="@lankacnews",
                                count=200,
                                lang="en",
                              since=datetime.datetime(2021, 5, 1, 0, 0, 0),
                                include_rts=False,
                                tweet_mode='extended'
                                );
    lankadeepa = api.user_timeline(screen_name="@LankadeepaNews",
                                count=200,
                                lang="en",
                                   since=datetime.datetime(2021, 5, 1, 0, 0, 0),
                                include_rts=False,
                                tweet_mode='extended'
                                );
    bbcSinhala = api.user_timeline(screen_name="@bbcsinhala",
                                   count=200,
                                   lang="en",
                                   since=datetime.datetime(2021, 5, 1, 0, 0, 0),
                                   include_rts=False,
                                   tweet_mode='extended'
                                   );
    hiruNews = api.user_timeline(screen_name="@hirunews",
                                   count=200,
                                   lang="en",
                                 since=datetime.datetime(2021, 5, 1, 0, 0, 0),
                                   include_rts=False,
                                   tweet_mode='extended'
                                   );
    all_tweets=[];
    final_tweets=[];
    all_tweets.extend(adaDerana);
    all_tweets.extend(cNews);
    all_tweets.extend(lankadeepa);
    all_tweets.extend(bbcSinhala);
    all_tweets.extend(hiruNews);

    for tweet in all_tweets:
        if tweet.created_at > datetime.datetime(2021, 5, 1, 0, 0, 0):
            final_tweets.append(tweet)

    outtweets = [[tweet.created_at,
                  tweet.full_text.encode("utf-8").decode("utf-8")]
                 for idx, tweet in enumerate(final_tweets)]


    df = DataFrame(outtweets, columns=["created_at", "text"])
    df.to_csv('sinhala_tweets_updated.csv', index=False)
    print(df)


# Driver code
if __name__ == '__main__':
    get_tweets()