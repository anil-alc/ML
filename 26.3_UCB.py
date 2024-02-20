# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:05:19 2022

@author: Anıl Alkan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler= pd.read_csv('Ads_CTR_Optimisation.csv')

import random
import math

N=10000     #tıklama
d=10        #total ilan
#Ri(n)
oduller= [0] * d    #ilk ilanların ödülü 0
#Ni(n)
tiklamalar= [0] * d 
toplam=0
secilenler= []
for n in range(1,N):
    ad=0 #seçilen ilan
    max_ucb=0
    
    for i in range(0,d):
        if(tiklamalar[i] > 0):
            ortalama= oduller[i] / tiklamalar[i]
            delta= math.sqrt(3/2 * math.log(n) / tiklamalar[i])
            ucb= ortalama + delta
        else:
            ucb= N*10
        if max_ucb < ucb:
            max_ucb= ucb
            ad=i            
    secilenler.append(ad)  
    tiklamalar[ad] = tiklamalar[ad] + 1 
    odul= veriler.values[n, ad]
    oduller[ad]= oduller[ad] + odul
    toplam= toplam + odul

print('Toplam Ödül')
print(toplam)   

plt.hist(secilenler)
plt.show()
    
