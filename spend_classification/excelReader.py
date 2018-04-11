# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:59:25 2018

@author: Vipin Kumar
"""

import pandas as pd
import numpy as np

def myfunc1(x):
    if(type(x)=='Str'):
       return  x.replace('!','')
    else :
        return x


def main(inputFile,outFile):

    xl = pd.ExcelFile(inputFile)

    # Print the sheet names
    print(xl.sheet_names)

    # Load a sheet into a DataFrame by name: df1
    df1 = xl.parse('Data')

    print(df1.columns.values)
    df2=df1[['Division Desc','Cost Centre Desc','Nominal Desc','Line Type' ,'Dist Desc','L1']]

    df3=df2.apply(np.vectorize(myfunc1))

    df3.to_csv(outFile, sep='!', encoding='utf-8')

    #writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')
    # Write your DataFrame to a file
    #df2.to_excel(writer, 'Sheet1')
    # Save the result
    #writer.save()


if __name__ == '__main__':
    main()