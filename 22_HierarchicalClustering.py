# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:22:37 2022

@author: Anıl Alkan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler= pd.read_csv("https://bilkav.com/musteriler.csv")

X= veriler.iloc[:,2:4].values


#HC
from sklearn.cluster import AgglomerativeClustering
ac= AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
Y_tahmin=ac.fit_predict(X)
print(Y_tahmin)

plt.scatter(X[Y_tahmin==0,0], X[Y_tahmin==0,1], s=100, c='red')
plt.scatter(X[Y_tahmin==1,0], X[Y_tahmin==1,1], s=100, c='blue')
plt.scatter(X[Y_tahmin==2,0], X[Y_tahmin==2,1], s=100, c='green')
plt.show()

#Scipy dendrogram
import scipy.cluster.hierarchy as sch
dendrogram= sch.dendrogram(sch.linkage(X, method='ward'))
plt.show()