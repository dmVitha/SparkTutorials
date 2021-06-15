import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

customer_data = pd.read_csv('shopping-data.csv')
customer_data.shape
data = customer_data.iloc[:, 3:4].values

plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='ward'))



cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')

print(cluster.fit_predict(data))