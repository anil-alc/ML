# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 00:06:37 2021

@author: Anıl Alkan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler= pd.read_csv("C:/Users/Anıl Alkan/Desktop/Python ile makine öğrenmesi/eksikveriler.csv")
#print(veriler)


#eksik veriler
from sklearn.impute import SimpleImputer

imputer= SimpleImputer(missing_values=np.nan, strategy='mean')

Yas= veriler.iloc[:,1:4].values
print(Yas)
imputer= imputer.fit(Yas[:,1:4])
Yas[:,1:4]= imputer.transform(Yas[:,1:4])
print(Yas)

print(Yas[:,1:4])

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

print(list(range(22)))
sonuc= pd.DataFrame(data=ulke, index=range(22), columns=['fr','tr','us'])
print(sonuc)

sonuc2= pd.DataFrame(data=Yas, index=range(22), columns=['boy','kilo','yas'])
print(sonuc2)

cinsiyet= veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3= pd.DataFrame(data=cinsiyet, index=range(22), columns=['cinsiyet'])
print(sonuc3)

s= pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split(s,sonuc,test_size=0.33, random_state=0)
