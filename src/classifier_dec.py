#importing important library
#task is to determine the player based on the attributes/features
import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

#matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("../data/Shakespeare_data.csv")
data.drop(data.index[:3], inplace=True)
data_object = data
data_object = data_object.fillna(data['ActSceneLine'].value_counts().index[0])
#Encoding the Plays categories
play_labels = data_object['Play'].astype('category').cat.categories.tolist()
play_category = {'Play' : {k: v for k,v in zip(play_labels,list(range(1,len(play_labels)+1)))}}

data_object.replace(play_category, inplace=True)
feature_names = ['PlayerLinenumber','Play']
x = data_object[feature_names]
y = data_object['Player']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
#Importing the Decision tree classifier from the sklearn library.
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion = 'entropy')
#Training the decision tree classifier. 
clf.fit(x_train, y_train)
#Predicting labels on the test set.
y_pred =  clf.predict(x_test)
#Importing the accuracy metric from sklearn.metrics library

from sklearn.metrics import accuracy_score
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(x_train)))
print('Accuracy Score on test data: ', accuracy_score(y_true=y_test, y_pred=y_pred))

