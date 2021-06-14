# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:28:28 2020

@author: Hiri
"""
#--------------------------------------------------------------
'''
The main model trained with Artificial Neural Network and saved by .h5
'''

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.metrics import accuracy_score

#import dataset
df = pd.read_csv('diabetes.csv')
X = df.iloc[:,:-1]
Y = df.iloc[:,[-1]]

#scale dataset
def scale(data):
  X = data
  scaler = StandardScaler()
  X = scaler.fit_transform(X)
  return X

# Neural network model
def model(inp):
  model = Sequential()
  model.add(Dense(5, input_dim=inp, activation='relu'))
  model.add(Dense(60, activation='relu'))
  model.add(Dropout(.2))
  model.add(Dense(24, activation='relu'))
  # model.add(Dropout(.4))
  model.add(Dense(16, activation='relu'))
  # # model.add(Dropout(.2))
  # model.add(Dense(4, activation='relu'))
  model.add(Dense(2, activation='softmax'))
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  return model




X = X.copy()
X = X.loc[:,['Npreg','Glu','Insulin','BMI','Age']]
x = scale(X)
x = pd.DataFrame(x, columns = (col for col in X.columns))
y = Y.copy()


ohe = OneHotEncoder()
y = ohe.fit_transform(y).toarray()
#split the data by train and test
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
print(X_train.shape)

model = model(len(X_train.columns))
history = model.fit(X_train, y_train, epochs=150, batch_size=170,validation_data=(X_test,y_test))

y_pred = model.predict(X_test)
#Converting predictions to label
pred = list()

for i in range(len(y_pred)):
    pred.append(np.argmax(y_pred[i]))
#Converting one hot encoded test label to label
test = list()
for i in range(len(y_test)):
    test.append(np.argmax(y_test[i]))



a = accuracy_score(pred,test)
print('---------> Accuracy is:', a*100,'%')

#save model
model.save('model_ANN.h5')