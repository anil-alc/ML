import numpy as np 
import pandas as pd
import re

yorumlar= pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)



import nltk 

durma= nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()

nltk.download('stopwords')
from nltk.corpus import stopwords


derleme=[]
for i in range(1000):
    yorum= re.sub('[^a-zA-Z]',' ',yorumlar['Review'][i])
    yorum= yorum.lower()
    yorum= yorum.split()
    yorum= [ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words('english'))]
    yorum= ' '.join(yorum)
    derleme.append(yorum)
    
from sklearn.feature_extraction.text import CountVectorizer
cv= CountVectorizer(max_features=1000)
X= cv.fit_transform(derleme).toarray() #bağımsız değ.
y= yorumlar.iloc[:,1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.20)

from sklearn.naive_bayes import GaussianNB
gnb= GaussianNB()
gnb.fit(X_train, y_train)

y_pred= gnb.predict(X_test)

from sklearn.metrics import confusion_matrix 
cm= confusion_matrix(y_test, y_pred)
print(cm)   