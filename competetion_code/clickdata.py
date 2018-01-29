# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:06:33 2017

@author: Vipin Kumar
"""
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import hashlib

def myfunc(x):
    return int(hashlib.sha1(x).hexdigest(), 16) % (10 ** 8)

def main():
    # Set seed for reproducibility
    np.random.seed(0)

    print("Loading data...")
    # Load the data from the CSV files
    
    training_data = pd.read_csv('/home/vipin/Videos/train.csv', header=0)
    prediction_data = pd.read_csv('/home/vipin/Videos/test.csv', header=0)
     
     
    training_data['countrycode']=training_data['countrycode'].apply(lambda x:ord(x))
    training_data['browserid']=training_data['browserid'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown") )
    training_data['devid']=training_data['devid'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("none"))
    
    
    #pd.to_csv('/home/vipin/Videos/train11.csv', sep=',', encoding='utf-8')
    #exit(0)
    prediction_data['countrycode']=prediction_data['countrycode'].apply(lambda x:ord(x))
    prediction_data['browserid']=prediction_data['browserid'].apply(lambda x:myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown") )
    prediction_data['devid']=prediction_data['devid'].apply(lambda x:myfunc (x) if np.all(pd.notnull(x)) else myfunc("none") )
    
    
    features=['siteid','offerid','category','merchant','countrycode','browserid','devid']
    target="click"
    X = training_data[features]
    x_prediction = prediction_data[features]
    Y= training_data[target]
    ids = prediction_data["ID"]
    model = XGBClassifier()
            
            
    #linear_model.LogisticRegression(n_jobs=-1)
        
    print("Training...")
            # Your model is trained on the training_data
    model.fit(X, Y)
        
    print("Predicting...")
    
    seed =7
    test_size=0.33
    X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=test_size,random_state=seed)
    y_prediction = model.predict_proba(x_prediction)
    results = y_prediction[:, 1]
    results_df = pd.DataFrame(data={'probability':results})
    joined = pd.DataFrame(ids).join(results_df)
        
    y_pred=model.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    

    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    print("Writing predictions to predictions.csv")
        # Save the predictions out to a CSV file
    joined.to_csv("/home/vipin/Videos/predictions.csv", index=False)
        # Now you can upload these predictions on numer.ai
    
if __name__ == '__main__':
    main()
    