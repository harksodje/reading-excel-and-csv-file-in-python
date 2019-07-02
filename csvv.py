# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:27:38 2019

@author: HP
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
a = pd.read_csv('pivot.csv') #importing the set 
#print (a)
b= pd.pivot_table(a, index=['continent'], columns=['year'],values=['lifeExp'])
print (b) #pivoting the set data
a1= b.to_csv('adex',encoding='utf-8') #saving data in csv format
print (sns.heatmap(b,linewidth=0.5, vmin=20,
                   vmax=100,center=0,annot=True,cmap="Spectral_r" )) #plotting the pivoted table using seasborn

