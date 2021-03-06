# -*- coding: utf-8 -*-
" ANNtest.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T_xskjCaA_EYFZExMAgbl7W_G90w1OvE
"""

import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import keras

 
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix

data=pd.read_csv("hdd.csv")
data

"""import matplotlib
matplotlib.use('Agg')
"""

data.describe()

data.isnull().any()

data=data.dropna()
data

print(data.shape)
print(data.dtypes)

# plot histograms for each variable
data.hist(figsize = (12, 12))
plt.show()

pd.crosstab(data.age,data.target).plot(kind="bar",figsize=(20,6))
plt.title('Heart Disease Frequency for Ages')
plt.xlabel('age')
plt.ylabel('Frequency')
plt.show()

import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns

plt.figure(figsize=(10,10))
sns.heatmap(data.corr(),annot=True,fmt='.1f')
plt.show()

X = data.iloc[:,:13].values
y = data["target"].values
!pip install sklearn

from sklearn.model_selection import train_test_split

X_train,X_test,y_train, y_test = train_test_split(X,y,test_size = 0.2 , random_state = 0 )

classifier=Sequential()

classifier.add(Dense(activation="sigmoid",input_dim=13,units=8,kernel_initializer="uniform"))
classifier.add(Dense(activation="sigmoid",units=8,kernel_initializer="uniform"))
classifier.add(Dense(activation="sigmoid",units=1,kernel_initializer="uniform"))
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

history=classifier.fit(X_train , y_train , batch_size =16,epochs =3500)

history.history.keys()

plt.plot(history.history['accuracy'])


plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])


plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

cm = confusion_matrix(y_test,y_pred)
cm

accuracy = (cm[0][0]+cm[1][1])/(cm[0][1] + cm[1][0] +cm[0][0] +cm[1][1]) 
print(accuracy*100)

TN,FP,FN,TP = confusion_matrix(y_test, y_pred).ravel()

TN

FP

FN

TP

"""#f1 score calculation for the model.

Precision=TP/TP+FP
"""

Precision=TP/(TP+FP)
Precision

"""Recall=TP/TP+FN

"""

Recall=TP/(TP+FN)
Recall

"""#f1 score using precision and recall of the model


"""

f1=2*Precision*Recall/(Precision+Recall)
f1

"""#Accuracy comparison with Random Forest Method

"""

from sklearn.ensemble import RandomForestClassifier

import pandas as pd

data1 = pd.read_csv('/content/hdd.csv')
data1

from sklearn.model_selection import train_test_split
X = data1.iloc[:,:13].values
y = data1["target"].values

clf=RandomForestClassifier(n_estimators=100)

X_train,X_test,y_train, y_test = train_test_split(X,y,test_size = 0.2 , random_state = 0 )

clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

cm1 = confusion_matrix(y_test,y_pred)
cm1

accuracy = (cm1[0][0]+cm1[1][1])/(cm[0][1] + cm1[1][0] +cm1[0][0] +cm1[1][1]) 
print(accuracy*100)

TN,FP,FN,TP = confusion_matrix(y_test, y_pred).ravel()

Recall=TP/(TP+FN)
Recall

Precision=TP/(TP+FP)
Precision

f1=2*Precision*Recall/(Precision+Recall)
f1

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv("hdd.csv")

X = data.iloc[:,:13].values
y = data["target"].values
!pip install sklearn

classifier = LogisticRegression(solver='lbfgs',random_state=0)
X_train,X_test,y_train, y_test = train_test_split(X,y,test_size = 0.2 , random_state = 0 )

classifier.fit(X_train, y_train)
predicted_y = classifier.predict(X_test)

print('Accuracy: {:.2f}'.format(classifier.score(X_test, y_test)))

