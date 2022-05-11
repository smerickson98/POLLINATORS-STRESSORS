#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:17:25 2022

@author: shannonerickson
"""
#THIS SCRIPT USES DATA FROM THE BeeColonies-05-12-2016.pdf FROM 
#https://usda.library.cornell.edu/concern/publications/rn301137d?locale=en
#THE DATA USED IS 2015 QUARTERLY DATA, NOT DATA FROM THE FIRST QUARTER OF 2016 AND WAS USED TO CREATE 2 CSV FILES 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#use pdf from honeybee survey to create a csv for yearly population data of bees

columns = ['state','colonies','max colonies','lost colonies','percent lost','added colonies','renovated colonies','percent renovated']
b15 = pd.read_csv('beespop2015.csv', usecols=columns)
#show columns and read yearly csv data

b15.drop('colonies', inplace=True, axis=1)
b15.drop('percent lost', inplace=True, axis=1)
b15.drop('added colonies', inplace=True, axis=1)
b15.drop('renovated colonies', inplace=True, axis=1)
b15.drop('percent renovated', inplace=True, axis=1)
#drop columns as needed


b15['max colonies'] = b15['max colonies'].astype('int')
b15['lost colonies'] = b15['lost colonies'].astype('int')
#turn columns into integers
b15['max colonies'] = b15['max colonies'].replace(np.nan, 0)
b15['lost colonies'] = b15['lost colonies'].replace(np.nan, 0)
#fill in zeros
groups1 = b15.groupby(['state'])['max colonies'].sum()
groups2 = b15.groupby(['state'])['lost colonies'].sum()
loss = (groups2/groups1)*100
#group to create percentages of loss for the total year (pdf was in quarter data)
losses15 = list(loss.items())
#create a list of groups

def Sort_Tuple(losses15):
    losses15.sort(key = lambda x: x[1])
    return losses15
#sort the data
print('\nORDERED BEE LOSSES BY STATE 2015', '\n', Sort_Tuple(losses15), '\n')
#show state order with percents of bee losses
bee15 = Sort_Tuple(losses15)
pd.DataFrame(bee15, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2015 TOTAL CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('2015TOTALSTATECCDLOSSES.png')
plt.show()
#create graph showing bee loss percentage from states from CCD

lowest_losses15 = bee15[0:3]
print('\n3 LOWEST LOSSES BY STATE IN 2015', '\n', lowest_losses15, '\n')

highest_losses15 = bee15[-3:]
print('\n3 HIGHEST LOSSES BY STATE IN 2015', '\n', highest_losses15, '\n')

top_low_15 = lowest_losses15 + highest_losses15
print('\nTOP AND LOW STATES', top_low_15)
#show states with highest and lowest bee loss

pd.DataFrame(top_low_15, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2015 HIGHEST AND LOWEST STATE CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('HIGHESTANDLOWESTSTATECCDLOSSES2015.png')
plt.show()
#create graph of the top 3 and bottom 3 states by losses


#use the pdf to create a csv of the annual amount of colonies affected by CCD stressors
columns = ['varroamites','pests','diseases','pesticides','other','unknown']
c15 = pd.read_csv('ccd_2015.csv', usecols=columns)


print(c15)
#print out c15 data and copy over into lists
stressors = ['varroamites', 'pests', 'diseases', 'pesticides', 'other', 'unknown']
percentages = [19.8, 12.5, 2.2, 4.9, 15.5, 20.8]

#create a pie chart of the colony collapse stressors 
fig = plt.figure(figsize =(10, 7))
plt.pie(percentages, labels = stressors)
plt.title('% OF COLONIES AFFECTED BY STRESSORS IN 2015')
plt.savefig('PIECHART2015STRESSORSFORUS.png')
plt.show()






