# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:53:12 2022

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

#Ni(n)
toplam=0
secilenler= []
birler= [0] * d
sifirlar= [0] * d
for n in range(1,N):
    ad=0 #seçilen ilan
    max_th=0
    
    for i in range(0,d):
        rasbeta= random.betavariate(birler[i]+1, sifirlar[i]+1)
        if rasbeta > max_th:
            max_th = rasbeta
            ad=i
            
           
    secilenler.append(ad) 
    odul= veriler.values[n, ad]
    if odul == 1:
        birler[ad] = birler[ad]+1
    else:
        sifirlar[ad]= sifirlar[ad]+1
    
    toplam= toplam + odul

print('Toplam Ödül')
print(toplam)   

plt.hist(secilenler)
plt.show()
