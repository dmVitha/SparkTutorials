import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt
import dateutil.parser
import datetime
from nltk.corpus import stopwords
import re
import string
import csv
import nltk
from nltk.util import ngrams
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import defaultdict
import codecs

def tweets_preprocess():
    tweets = pd.read_csv(r'C:\Users\Dulan\PycharmProjects\SparkTutorials\news_collection.csv')
    df = pd.DataFrame(tweets, columns=['created_at', 'text'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['text'] = df['text'].apply(lambda x: str(x))

    pd.set_option('display.max_colwidth', 0)

    df = df.groupby(pd.Grouper(key='created_at', freq='1D')).agg(lambda x: ' '.join(set(x)))
    df["text"] = df["text"].apply(lambda x: remove_punct(x))
    df["text"] = df["text"].apply(lambda x: stemming(x))
    # df["text"] = df["text"].apply(lambda x: generate_ngrams(x))

    return df



def remove_punct(text):
    text = re.sub('https?://\S+|www\.\S+', '', text)
    # text = "".join([char for char in text if char not in string.punctuation])
    # text = [word for word in text if word not in stopwords]
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[’“”…\-]', '', text)
    text = re.sub(r'[0-9]','',text)
    # retweet
    text = re.sub('RT|‘', '', text)
    # removing the stop-words
    text_tokens = word_tokenize(text)
    stop_words = remove_stopwords()
    tokens_without_sw = [word for word in text_tokens if not word in stop_words]
    filtered_sentence = (" ").join(tokens_without_sw)
    text = filtered_sentence

    return text


def tokenize(text):
    return nltk.word_tokenize(text)


def remove_stopwords():
    with open("stopWords.txt", 'r', encoding="utf8") as file_handle:
        stopwords = file_handle.read().splitlines()
    # text = [word for word in text if word not in stopwords]
    return stopwords


def stemming(text):
    stem_Dictionary = dict()
    file = open('stemDictionary.txt', 'r', encoding="utf8")
    for line in file:
        data = re.split('\s+', line)
        key, value = data[0], data[1]
        stem_Dictionary[key] = value

    token_words = word_tokenize(text)
    text = " ".join([stem_Dictionary.get(w, w) for w in token_words])
    return text


def generate_ngrams(text):
    n_grams = ngrams(nltk.word_tokenize(text), 1)
    return [' '.join(grams) for grams in n_grams]





# Driver code
if __name__ == '__main__':
    print(tweets_preprocess())
    tweets_preprocess().to_csv(r'C:\Users\Dulan\PycharmProjects\SparkTutorials\preprocessed_tweets.csv',index = True, header=True)
