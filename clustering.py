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
from collections import defaultdict, Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy.cluster.hierarchy as shc


def tweets_clustring():
    initial_distances = pairwise_distances(data, metric='euclidean')
    # making all the diagonal elements infinity
    np.fill_diagonal(initial_distances, sys.maxsize)
    indexes = minvalue_indexes(initial_distances)

    clusters = {}
    row_index = -1
    col_index = -1
    array = []

    for n in range(input.shape[0]):
        array.append(n)

    clusters[0] = array.copy()

    # finding minimum value from the distance matrix
    # note that this loop will always return minimum value from bottom triangle of matrix
    for k in range(1, input.shape[0]):
        min_val = sys.maxsize

        for i in range(0, input.shape[0]):
            for j in range(0, input.shape[1]):
                if (input[i][j] <= min_val):
                    min_val = input[i][j]
                    row_index = i
                    col_index = j

    for i in range(0, input.shape[0]):
        if (i != col_index and i != row_index):
            return i, j


def generate_ngrams(token, n):
    ngrams = zip(*[token[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


# Driver code
if __name__ == '__main__':
    tweets_clustering()
