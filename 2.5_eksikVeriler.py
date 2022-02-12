# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:02:33 2021

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