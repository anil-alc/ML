
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


#K-NN
from sklearn.neighbors import KNeighborsClassifier

knn= KNeighborsClassifier(n_neighbors=5, metric='minkowski')
knn.fit(X_train, y_train)
y_pred= knn.predict(X_test)

from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_pred)
print(cm)
