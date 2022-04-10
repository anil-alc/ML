# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 21:26:28 2022

@author: Anıl Alkan
"""
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

veriler= pd.read_csv("https://bilkav.com/veriler.csv")

x= veriler.iloc[:,1:4].values #bağımsız değ.
y= veriler.iloc[:,4:].values # bağımlı değ.

#Eğitim Test için bölüm
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.33, random_state=0)

#Verilerin ölçeklenmesi
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()

X_train= sc.fit_transform(x_train)
X_test= sc.transform(x_test)

#Confusion Matrix 
from sklearn.metrics import confusion_matrix




#Naive Bayes
from sklearn.naive_bayes import GaussianNB
gnb= GaussianNB()
gnb.fit(X_train, y_train)

y_pred= gnb.predict(X_test)
print("y pred")
print(y_pred)

cm= confusion_matrix(y_test,y_pred)
print("GNB CM")
print(cm)


