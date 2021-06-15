# -*- coding: utf-8 -*-
import numpy as np
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import pairwise_distances
import sys

def minvalue_indexes(scores):
    initial_distances = pairwise_distances(scores, metric='euclidean')
    np.fill_diagonal(initial_distances, sys.maxsize)

    for k in range(1, initial_distances.shape[0]):
        min_val = sys.maxsize

        for i in range(0, initial_distances.shape[0]):
            for j in range(0, initial_distances.shape[1]):
                if (initial_distances[i][j] <= min_val):
                    min_val = initial_distances[i][j]
                    row_index = i
                    col_index = j


    for i in range(0, initial_distances.shape[0]):
        if (i != col_index and i != row_index):
            return i,j


def find_clusters(keywords,scores):
    no_of_titles=len(keywords)
    keyword_score= np.array(scores).reshape(no_of_titles,1)
    cluster = AgglomerativeClustering(n_clusters=None, affinity='euclidean', linkage='average', distance_threshold=0.5)
    cluster.fit(keyword_score)
    labels = cluster.labels_
    topics_final = []
    for index in range(cluster.n_clusters_):
        topics = []
        for i, val in enumerate(labels):
            if val == index:
                topics.append(keywords[i])
        topics_final.append(topics)
    return topics_final

def generate_ngrams(text):
    n_grams = ngrams(nltk.word_tokenize(text), 3)
    return [' '.join(grams) for grams in n_grams]

# Driver code
if __name__ == '__main__':
    tweets = pd.read_csv(r'C:\Users\Dulan\PycharmProjects\SparkTutorials\preprocessed_tweets.csv')

    df = pd.DataFrame(tweets, columns=['created_at', 'text'])
    df["text"] = df["text"].apply(lambda x: generate_ngrams(x))

    inp={}
    for index in df.index:
        inp[df["created_at"][index]]=df["text"][index]


    no_of_days = df.shape[0]
    first_day=df.iloc[0, df.columns.get_loc('created_at')]
    count = {}


    for dateIdx, date in enumerate(sorted(inp)):
        for keywordIndex, keyword in enumerate(inp[date]):
            if keyword not in count:
                count[keyword] = [0] * no_of_days
            count[keyword][dateIdx] += 1

    res = {}
    dates = sorted(inp.keys())
    for date in dates:
        res[date] = {}

    for keyword in count:
        for cIdx, c in enumerate(count[keyword]):
            if cIdx > 0 and count[keyword][cIdx] > 0:
                res[dates[cIdx]][keyword] = round((count[keyword][cIdx]+1)/(np.log((sum(count[keyword][0:cIdx]) / cIdx)+1)+1),2)

    del res[first_day]
    # print(res)
    for key,val in res.items():
        keywords = []
        scores=[]
        for index in val:
            keywords.append(index)
            scores.append(val[index])
            # data_dict[index]=val[index]
        # find_clusters(keywords,scores,no_of_clusters)
        print(key)
        print(keywords)
        print(scores)
        # for i in find_clusters(keywords,scores):
        #     print(i)
        print("--------------------------------------------------------------------------")






