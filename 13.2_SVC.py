# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:22:52 2022

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




#SVM
from sklearn.svm import SVC
svc= SVC(kernel='linear')
svc.fit(X_train, y_train)
y_pred= svc.predict(X_test)

cm= confusion_matrix(y_test, y_pred)
print('SVC')
print(cm)
