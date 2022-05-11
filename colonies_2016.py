#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 00:41:07 2022

@author: shannonerickson
"""

#THIS SCRIPT USES DATA FROM THE BeeColonies-08-01-2017.pdf FROM 
#https://usda.library.cornell.edu/concern/publications/rn301137d?locale=en
#THE DATA USED IS 2016 QUARTERLY DATA, NOT DATA FROM THE FIRST QUARTER OF 2017 AND WAS USED TO CREATE 2 CSV FILES 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#use pdf from honeybee survey to create a csv for yearly population data of bees

columns = ['state','colonies','max colonies','lost colonies','percent lost','added colonies','renovated colonies','percent renovated']
b16 = pd.read_csv('beespop2016.csv', usecols=columns)
#show columns and read yearly csv data

b16.drop('colonies', inplace=True, axis=1)
b16.drop('percent lost', inplace=True, axis=1)
b16.drop('added colonies', inplace=True, axis=1)
b16.drop('renovated colonies', inplace=True, axis=1)
b16.drop('percent renovated', inplace=True, axis=1)
#drop columns as needed


b16['max colonies'] = b16['max colonies'].astype('int')
b16['lost colonies'] = b16['lost colonies'].astype('int')
#turn columns into integers
b16['max colonies'] = b16['max colonies'].replace(np.nan, 0)
b16['lost colonies'] = b16['lost colonies'].replace(np.nan, 0)
#fill in zeros
groups1 = b16.groupby(['state'])['max colonies'].sum()
groups2 = b16.groupby(['state'])['lost colonies'].sum()
loss = (groups2/groups1)*100
#group to create percentages of loss for the total year (pdf was in quarter data)
losses16 = list(loss.items())
#create a list of groups

def Sort_Tuple(losses16):
    losses16.sort(key = lambda x: x[1])
    return losses16
#sort the data
print('\nORDERED BEE LOSSES BY STATE 2016', '\n', Sort_Tuple(losses16), '\n')
#show state order with percents of bee losses
bee16 = Sort_Tuple(losses16)
pd.DataFrame(bee16, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2016 TOTAL CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('2016TOTALSTATECCDLOSSES.png')
plt.show()
#create graph showing bee loss percentage from states from CCD

lowest_losses16 = bee16[0:3]
print('\n3 LOWEST LOSSES BY STATE IN 2016', '\n', lowest_losses16, '\n')

highest_losses16 = bee16[-3:]
print('\n3 HIGHEST LOSSES BY STATE IN 2016', '\n', highest_losses16, '\n')

top_low_16 = lowest_losses16 + highest_losses16
print('\nTOP AND LOW STATES 2016', top_low_16)
#show states with highest and lowest bee loss

pd.DataFrame(top_low_16, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2016 HIGHEST AND LOWEST STATE CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('HIGHESTANDLOWESTSTATECCDLOSSES2016.png')
plt.show()
#create graph of the top 3 and bottom 3 states by losses


#use the pdf to create a csv of the annual amount of colonies affected by CCD stressors
columns = ['varroamites','pests','diseases','pesticides','other','unknown']
c16 = pd.read_csv('ccd_2016.csv', usecols=columns)


print(c16)
#print out c15 data and copy over into lists
stressors = ['varroamites', 'pests', 'diseases', 'pesticides', 'other', 'unknown']
percentages = [17.6, 13.4, 2.2,	4.1, 10.4, 16.1]

#create a pie chart of the colony collapse stressors 
fig = plt.figure(figsize =(10, 7))
plt.pie(percentages, labels = stressors)
plt.title('% OF COLONIES AFFECTED BY STRESSORS IN 2016')
plt.savefig('PIECHART2016STRESSORSFORUS.png')
plt.show()


