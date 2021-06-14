# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:17:54 2020

@author: Hiri
"""
#-----------------------------------------------------------------
'''
other model trained with Random Forest and seved with .pkl
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('diabetes.csv')

X = df.iloc[:,:-1]
Y = df.iloc[:,[-1]]


x = X.copy()
x = x.loc[:,['Npreg','Glu','BMI','Age']]
#x = scale(x)
y = Y.copy()
x = pd.DataFrame(x, columns = (col for col in x.columns))
df_ScalDrop = pd.concat([x,y],axis=1)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)


model = RandomForestClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print("accuracy validation for RF is : ",metrics.accuracy_score(y_test,y_pred))
print('----------------------------------------------------')

from sklearn.externals import joblib
joblib.dump(model,'model_RF.pkl')