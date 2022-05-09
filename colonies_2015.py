#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:17:25 2022

@author: shannonerickson
"""

#delete and drop the extra rows
#rename the columns to be more clear in the csv

#a file that has multiple header rows
#dataframe = pd.read_csv('x.csv', header=[0,1,2,...])
#print(dataframe)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2015 colony population data
#lost colonies,percent lost,added colonies,renovated colonies,percent renovated
columns = ['state','colonies','max colonies','lost colonies','percent lost','added colonies','renovated colonies','percent renovated']
b15 = pd.read_csv('beespop2015.csv', usecols=columns)
#columns.filna(0, inplace=True)

b15.drop('colonies', inplace=True, axis=1)
b15.drop('percent lost', inplace=True, axis=1)
b15.drop('added colonies', inplace=True, axis=1)
b15.drop('renovated colonies', inplace=True, axis=1)
b15.drop('percent renovated', inplace=True, axis=1)
#bees2015 = bees2015.drop(bees2015.index[1:9, 64:80, 135:149, 204:219, 273:])

#print(b15)

b15['max colonies'] = b15['max colonies'].astype('int')
b15['lost colonies'] = b15['lost colonies'].astype('int')

b15['max colonies'] = b15['max colonies'].replace(np.nan, 0)
b15['lost colonies'] = b15['lost colonies'].replace(np.nan, 0)

groups1 = b15.groupby(['state'])['max colonies'].sum()
groups2 = b15.groupby(['state'])['lost colonies'].sum()
loss = (groups2/groups1)*100

losses15 = list(loss.items())

x_val = [x[0] for x in losses15]
y_val = [x[1] for x in losses15]

plt.bar(x_val, y_val)
plt.title('2015 CCD Losses')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.show()
#print(x_val)
#all([isinstance(item, int) for item in x_val])
##print(y_val)
#print(type(y_val))
#all([isinstance(item, int) for item in y_val])
#plt.plot(x_val,y_val)
#plt.plot(x_val,y_val,'or')
#plt.show()
#print(losses15)
#new = loss.to_string()
#print(new)
#print('\nHIGH PEST', '\n', groups.to_string(),'\n')
#loss.set_index(None)
#state = b15['state']


#%%loss.plot()
#####loss.plot()
#####fig = plt.figure(figsize = (10,5))
#####plt.bar(loss, width =.5, height = loss)
#ax = fig.add_axes
#fig = plt.figure(figsize = (10, 5))
#plt.bar(state, loss)
#plt.title('Bees and CCD 2015')
#plt.xlabel('State')
#plt.ylabel('Loss of Colonies from CCD indicators (%)')
#plt.bar(loss, height = 10, color='b', width=width)
#plt.ticklabel_format(style='plain')
#plt.legend(fontsize=4)
#plt.legend(fontsize=5, bbox_to_anchor=(1.02, 1), loc='upper right', borderaxespad=0)
#plt.figure(dpi=300)
#plt.savefig('BEES15CCDDD.png')
#plt.show()

#print(loss)
#groups = b15.groupby(['state'])['max colonies', 'lost colonies'].sum()
#totals = groups['hp_kg'].sum()
#groups.unstack.plot()








