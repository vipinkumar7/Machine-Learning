# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 14:25:32 2014

@author: hduser2
"""

import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#### Variables to Set ####
test_split = .33
########################## 

def getDataset(filename):
    read = open(filename)
    data = []
    for line in read:
        data.append( np.array([ float(x) for x in line.split("\t") ]) )
    return np.array(data)
    

data1 = getDataset("onebytwo.txt")
labels1 = np.zeros(len(data1))

data2 = getDataset("onebythree.txt")
labels2 = np.ones(len(data1))

data3 = getDataset("onebysix.txt")
labels3 = np.ones(len(data1)) * [2]



data = np.vstack((data1,data2,data3))
print "data shape:",data.shape
labels = np.hstack((labels1,labels2,labels3))
print "labels shape:", labels.shape

print "Split Percentage:" , test_split
data_train, data_test, label_train, label_test = train_test_split(data, labels, test_size=test_split, random_state=42)


gnb = GaussianNB()
model = gnb.fit(data_train, label_train)
predictions = model.predict(data_test)

print classification_report(label_test, predictions)
print "Accuracy:", accuracy_score(label_test, predictions)
