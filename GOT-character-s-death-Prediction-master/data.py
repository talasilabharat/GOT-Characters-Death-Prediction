# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:45:47 2018

@author: Pooja
"""

import pandas as pd
import numpy as np

data=pd.read_csv("character-predictions.csv")        
       
data.title=data.title.astype('category')  
data.culture=data.culture.astype('category')        
data.name=data.name.astype('category')
data.house=data.house.astype('category')

#converting categorical to numerical values
cat_columns = data.select_dtypes(['category']).columns
data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes)

#converting title column based on importance
unique,counts=np.unique(data['title'],return_counts=True)
diction=dict(zip(unique,counts))
data['title']=data['title'].apply(lambda x: 1/diction[x])   