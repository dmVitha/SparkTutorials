import socket
import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt
import dateutil.parser
import  datetime
from nltk.corpus import stopwords
import re
import string
import csv
import nltk
from nltk.util import ngrams
from nltk.stem import PorterStemmer
from collections import defaultdict

def get_tweets():
    tweets = pd.read_csv(r'C:\Users\Dulan\PycharmProjects\SparkTutorials\sinhala_tweets.csv')
    df = pd.DataFrame(tweets, columns=['Created At', 'Text'])
    df['Created At'] = pd.to_datetime(df['Created At'])
    df['Text']=df['Text'].apply(lambda x:str(x))

    pd.set_option('display.max_colwidth', 1)

    df=df.groupby(pd.Grouper(key='Created At', freq='D')).agg(lambda x: ' '.join(set(x)))
    df["Text"]=df["Text"].apply(lambda x: remove_punct(x))

    # df["Text"] = df["Text"].apply(lambda x: re.sub(r'\b\w{1,2}\b', '', x))
    df["Text"]=df["Text"].apply(lambda x: tokenize(x))
    df["Text"] = df["Text"].apply(lambda x: remove_stopwords(x))
    df["Text"] = df["Text"].apply(lambda x: stemming(x))
    df["TextBigrams"] = df["Text"].apply(lambda x: list(nltk.bigrams(x)))
    # df["TextTriigrams"] = df["Text"].apply(lambda x: list(nltk.trigrams(x)))
    print(df)


def remove_punct(text):
    text = re.sub('https:\/\/.*', '', text)
    text  = "".join([char for char in text if char not in string.punctuation])
    # text = [word for word in text if word not in stopwords]
    text = re.sub('[0-9]+', '', text)
    text = re.sub('\n+', '', text)
    #retweet
    text= re.sub('RT', '', text)
    return text

def tokenize(text):
    return nltk.word_tokenize(text)

def remove_stopwords(text):
    with open("stopWords.txt", 'r',encoding="utf8") as file_handle:
        stopwords= file_handle.read().splitlines()
    text = [word for word in text if word not in stopwords]
    return text

def stemming(text):
    stem_Dictionary=dict()
    file = open('stemDictionary.txt', 'r',encoding="utf8")
    for line in file:
        data = re.split('\s+',line)
        key, value = data[0], data[1]
        stem_Dictionary[key] = value

    text=" ".join([stem_Dictionary.get(w,w) for w in text])
    return nltk.word_tokenize(text)








# Driver code
if __name__ == '__main__':
    get_tweets()
    # stemming("")
