# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:02:05 2021

@author: Anıl Alkan
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler= pd.read_csv("C:/Users/Anıl Alkan/Desktop/Python ile makine öğrenmesi/eksikveriler.csv")
#print(veriler)


#eksik veriler


ulke= veriler.iloc[:,0:1].values
print(ulke)
print("***************************")

from sklearn import preprocessing

le= preprocessing.LabelEncoder()

ulke[:,0]= le.fit_transform(veriler.iloc[:,0])
print(ulke)
print("***************************")

ohe= preprocessing.OneHotEncoder()
ulke= ohe.fit_transform(ulke).toarray()
print(ulke)