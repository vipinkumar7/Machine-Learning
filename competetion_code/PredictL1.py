# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:38 2018

@author: root
"""

import numpy as np
import pandas as pd
from sklearn import  linear_model
#from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
import hashlib

def myfunc(x):
    return int(hashlib.sha1(x).hexdigest(), 16) % (10 ** 8)

def myfunc1(x):
    if(x=='Non-Sourceable'):
        return 1
    elif (x=='T&E'):
        return 2
    elif(x=='Professional Services'):
        return 3
    elif(x=='FM'):
        return 4
    elif(x=='IT'):
        return 5
    elif(x=='Marketing'):
        return 6
    elif(x=='Unclassified'):
        return 7
    elif(x=='HR'):
        return 8
    elif(x=='Utilities'):
        return 9
    elif(x=='Logistics'):
        return 10
    else:
        return 0

        
def main():
    
    print("Loading data...")
    
    
    training_data = pd.read_csv('/home/vipin/Desktop/Invoice3.csv', header=0,delimiter="!")
 
    np.random.seed(0)


    training_data['Division Desc']=training_data['Division Desc'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown") ) 
    training_data['Cost Centre Desc']=training_data['Cost Centre Desc'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown") )
    training_data['Nominal Desc']=training_data['Nominal Desc'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown"))
    training_data['Line Type']=training_data['Line Type'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown"))
    training_data['Dist Desc']=training_data['Dist Desc'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown"))
    training_data['L1']=training_data['L1'].apply(lambda x: myfunc1 (x))


    
    features=['Division Desc' ,'Cost Centre Desc' ,'Nominal Desc' ,'Line Type','Dist Desc']
    target='L1'    
    
    X = training_data[features]
    
    
    
    Y= training_data[target]
    
    print(Y.isnull().sum())
    
    model = linear_model.LinearRegression() #XGBClassifier()
    
    
   
    seed =7
    test_size=0.33
    X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=test_size,random_state=seed)
    
    model.fit(X_train, y_train)
   
    
    y_pred=model.predict(X_test)
    #accuracy=accuracy_score(y_test,y_pred)
    

    acc=model.score(X_test,y_pred)
    print(acc)    
    print("Mean squared error: %.2f"
      % mean_squared_error(y_test,y_pred))
    #print("Accuracy: %.2f%%" % (accuracy * 100.0))
    
    print('Variance score: %.2f' % r2_score(y_test,y_pred))
if __name__ == '__main__':
    main()
    