# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 15:41:07 2014

@author: hduser2
"""

import numpy as np
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

opfile = open('mahout-inp.txt','w')

for rowNum in range(len(data)) :
    opfile.write("class_" + str(labels[rowNum]) + "\t")
    for colNum in range(len(data[rowNum])):
        #opfile.write("col_" + str(colNum)+ "_" + str(int(data[rowNum][colNum])) + " ")
        opfile.write(str(int(data[rowNum][colNum])) + " ")
    opfile.write("\n")
    
opfile.close()