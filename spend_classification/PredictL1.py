# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:38 2018

@author: Vipin Kumar
"""

import numpy as np
import pandas as pd
from sklearn import  linear_model
#from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import label_binarize
from sklearn import preprocessing
from  PlotPrecisionRecallCurve import  PrecisionRecallCurve
import hashlib


class PredictSpend():
    def __init__(self, inputFile):
        self.features=['Division Desc' ,'Cost Centre Desc' ,'Nominal Desc' ,'Line Type','Dist Desc']
        self.selectData=['Division Desc', 'Cost Centre Desc', 'Nominal Desc', 'Line Type', 'Dist Desc', 'L1']
        self.target=['L1']
        self.inputFile=inputFile

    def generateHash(self,x):
        return int(hashlib.sha1(str(x).encode('utf-8')).hexdigest(), 16) % (10 ** 8)

    def putUnknown(self,x):
        if x and x.strip():
            return x.lower()
        else:
            return "unknown"

    def predict(self):
        print("Loading data...")
        xl = pd.ExcelFile(self.inputFile)
        df1 = xl.parse('Data')
        print(df1.columns.values)
        training_data = df1[self.selectData]

        division_des=training_data['Division Desc'].apply(lambda x: self.generateHash (x) if np.all(pd.notnull(x)) else self.generateHash("unknown"))
        CCDesc=training_data['Cost Centre Desc'].apply(lambda x: self.generateHash (x) if np.all(pd.notnull(x)) else self.generateHash("unknown"))
        NDesc=training_data['Nominal Desc'].apply(lambda x: self.generateHash (x) if np.all(pd.notnull(x)) else self.generateHash("unknown"))
        Line_Type=training_data['Line Type'].apply(lambda x: self.generateHash (x) if np.all(pd.notnull(x)) else self.generateHash("unknown"))
        Dist_Desc=training_data['Dist Desc'].apply(lambda x: self.generateHash (x) if np.all(pd.notnull(x)) else self.generateHash("unknown"))

        Y=training_data['L1'].apply(lambda x: self.putUnknown(x))
        X = pd.DataFrame({'Division Desc': division_des,
                                  "Cost Centre Desc": CCDesc,
                                  "Nominal Des": NDesc,
                                  "Line TypeD": Line_Type,
                                  "Dist Desc": Dist_Desc
                                  }
                                 )
        model = linear_model.LinearRegression() #XGBClassifier()
        seed =7
        test_size=0.33
        label_encoder = preprocessing.LabelEncoder()
        label_encoder.fit(Y.unique())
        classes = list(range(len(label_encoder.classes_)))
        print(Y.unique())
        Y_transformed = label_encoder.transform(Y)
        Y_hat = label_binarize(Y_transformed, classes=classes)

        X_train,X_test,Y_train,Y_test=train_test_split(X,Y_hat,test_size=test_size,random_state=seed)
        model.fit(X_train, Y_train)
        Y_prediction=model.predict(X_test)
        plotting=PrecisionRecallCurve(Y_test,Y_prediction)
        plotting.plot_curve()


if __name__ == '__main__':
    p= PredictSpend("/Users/kvipin/Downloads/Invoice.xlsx")
    p.predict()
