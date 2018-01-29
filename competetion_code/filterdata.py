# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:32:04 2017

@author: root
"""
import pandas as pd
import numpy as np
import hashlib
from  datetime import datetime

k=int(hashlib.sha1("print").hexdigest(), 16) % (10 ** 8)

def myfunc(x):
    return int(hashlib.sha1(x).hexdigest(), 16) % (10 ** 8)
    
def dateFun(x):
    return (datetime.strptime(x, "%Y-%m-%d %H:%M:%S").weekday()+1)%7

def main():
    training_data = pd.read_csv('/home/vipin/Videos/train.csv', header=0)
    #prediction_data = pd.read_csv('/home/vipin/Videos/test.csv', header=0)
     
     
    training_data['countrycode']=training_data['countrycode'].apply(lambda x:ord(x))
    training_data['browserid']=training_data['browserid'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown") )
    training_data['devid']=training_data['devid'].apply(lambda x: myfunc (x) if np.all(pd.notnull(x)) else myfunc("none"))
    training_data['datetime']=training_data['datetime'].apply(lambda x:dateFun(x))
    training_data.to_csv('/home/vipin/Videos/train12.csv', sep=',', encoding='utf-8')
    
    #prediction_data['countrycode'].apply(lambda x:ord(x))
    #prediction_data['browserid'].apply(lambda x:myfunc (x) if np.all(pd.notnull(x)) else myfunc("unknown") )
    #prediction_data['devid'].apply(lambda x:myfunc (x) if np.all(pd.notnull(x)) else myfunc("none") )
    
    #prediction_data.to_csv('/home/vipin/Videos/test11.csv', sep=',', encoding='utf-8')
    
if __name__ == '__main__':
    main()