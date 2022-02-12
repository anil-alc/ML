# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:58:10 2021

@author: Anıl Alkan
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler= pd.read_csv("C:/Users/Anıl Alkan/Desktop/Python ile makine öğrenmesi/veriler.csv")

boy= veriler[["boy"]]
#print(boy)

boykilo= veriler[["boy", "kilo"]]
print(boykilo)

class insan:
    boy=180
    def kosmak(self,b):
        return b+10
ali=insan()
print(ali.kosmak(90))    