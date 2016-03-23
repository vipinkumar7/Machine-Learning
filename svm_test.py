# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from numpy import genfromtxt

from numpy import column_stack
import numpy

train_data = genfromtxt('/home/vipin/Documents/pythondev/numer.ai/numerai_training_data1.csv', delimiter=",")

test_data=genfromtxt('/home/vipin/Documents/pythondev/numer.ai/numerai_tournament_data1.csv', delimiter=",")

#xx, yy = np.meshgrid(np.linspace(-3, 3, 500),np.linspace(-3, 3, 500))
#np.random.seed(0)
#X = np.random.randn(300, 2)
#Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)

X=train_data[:,0:21]

Y=train_data[:,21]

Z=test_data[:,1:22]

O=test_data[:,0]

# fit the model
clf = svm.NuSVC(probability=True)
clf.fit(X, Y)

P=clf.predict_proba(Z)

L=column_stack((O,P))

numpy.savetxt('/home/vipin/Documents/pythondev/numer.ai/testo.csv',L,fmt='%10.9f', delimiter=',') 


# plot the decision function for each datapoint on the grid
#Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
#Z = Z.reshape(xx.shape)

"""
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
           origin='lower', cmap=plt.cm.PuOr_r)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2,
                       linetypes='--')
plt.scatter(X[:, 0], X[:, 1], s=30, c=Y, cmap=plt.cm.Paired)
plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()
"""