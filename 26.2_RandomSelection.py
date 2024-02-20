# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:46:02 2022

@author: Anıl Alkan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler= pd.read_csv('Ads_CTR_Optimisation.csv')

import random

N=10000
d=10
toplam=0
secilenler= []
for n in range(0,N):
    ad= random.randrange(d)
    secilenler.append(ad)
    odul= veriler.values[n, ad]
    toplam= toplam + odul


plt.hist(secilenler)
plt.show()    

