#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 01:00:23 2022

@author: shannonerickson
"""


#THIS SCRIPT USES DATA FROM THE BeeColonies-08-01-2018.pdf FROM 
#https://usda.library.cornell.edu/concern/publications/rn301137d?locale=en
#THE DATA USED IS 2017 QUARTERLY DATA, NOT DATA FROM THE FIRST QUARTER OF 2018 AND WAS USED TO CREATE 2 CSV FILES 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#use pdf from honeybee survey to create a csv for yearly population data of bees

columns = ['state','colonies','max colonies','lost colonies','percent lost','added colonies','renovated colonies','percent renovated']
b17 = pd.read_csv('beespop2017.csv', usecols=columns)
#show columns and read yearly csv data

b17.drop('colonies', inplace=True, axis=1)
b17.drop('percent lost', inplace=True, axis=1)
b17.drop('added colonies', inplace=True, axis=1)
b17.drop('renovated colonies', inplace=True, axis=1)
b17.drop('percent renovated', inplace=True, axis=1)
#drop columns as needed


b17['max colonies'] = b17['max colonies'].astype('int')
b17['lost colonies'] = b17['lost colonies'].astype('int')
#turn columns into integers
b17['max colonies'] = b17['max colonies'].replace(np.nan, 0)
b17['lost colonies'] = b17['lost colonies'].replace(np.nan, 0)
#fill in zeros
groups1 = b17.groupby(['state'])['max colonies'].sum()
groups2 = b17.groupby(['state'])['lost colonies'].sum()
loss = (groups2/groups1)*100
#group to create percentages of loss for the total year (pdf was in quarter data)
losses17 = list(loss.items())
#create a list of groups

def Sort_Tuple(losses17):
    losses17.sort(key = lambda x: x[1])
    return losses17
#sort the data
print('\nORDERED BEE LOSSES BY STATE 2017', '\n', Sort_Tuple(losses17), '\n')
#show state order with percents of bee losses
bee17 = Sort_Tuple(losses17)
pd.DataFrame(bee17, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2017 TOTAL CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('2017TOTALSTATECCDLOSSES.png')
plt.show()
#create graph showing bee loss percentage from states from CCD

lowest_losses17 = bee17[0:3]
print('\n3 LOWEST LOSSES BY STATE IN 2017', '\n', lowest_losses17, '\n')

highest_losses17 = bee17[-3:]
print('\n3 HIGHEST LOSSES BY STATE IN 2017', '\n', highest_losses17, '\n')

top_low_17 = lowest_losses17 + highest_losses17
print('\nTOP AND LOW STATES 2017', top_low_17)
#show states with highest and lowest bee loss

pd.DataFrame(top_low_17, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2017 HIGHEST AND LOWEST STATE CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('HIGHESTANDLOWESTSTATECCDLOSSES2017.png')
plt.show()
#create graph of the top 3 and bottom 3 states by losses


#use the pdf to create a csv of the annual amount of colonies affected by CCD stressors
columns = ['varroamites','pests','diseases','pesticides','other','unknown']
c17 = pd.read_csv('ccd_2017.csv', usecols=columns)


print(c17)
#print out c15 data and copy over into lists
stressors = ['varroamites', 'pests', 'diseases', 'pesticides', 'other', 'unknown']
percentages = [26.3, 18.2, 0, 5, 13, 22.2]

#create a pie chart of the colony collapse stressors 
fig = plt.figure(figsize =(10, 7))
plt.pie(percentages, labels = stressors)
plt.title('% OF COLONIES AFFECTED BY STRESSORS IN 2017')
plt.savefig('PIECHART2017STRESSORSFORUS.png')
plt.show()

