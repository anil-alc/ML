# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 23:54:16 2021

@author: Anıl Alkan
"""

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('C:/Users/Anıl Alkan/Desktop/Python ile makine öğrenmesi/satislar.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)

aylar= veriler[['Aylar']]
print(aylar)

satislar= veriler[['Satislar']]
print(satislar)

satislar2= veriler.iloc[:,:1].values
print(satislar2)
'''
x = veriler.iloc[:,1:4].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişken
print(y)
'''
#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

'''
from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)
print(y_pred)
print(y_test)
'''
Y_train= sc.fit_transform(y_train)
Y_test= sc.fit_transform(y_test)

#model inşası(linear reggresion) 
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,Y_train)




