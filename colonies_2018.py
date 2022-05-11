#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 01:12:48 2022

@author: shannonerickson
"""

#THIS SCRIPT USES DATA FROM THE hcny0819.pdf FROM 
#https://usda.library.cornell.edu/concern/publications/rn301137d?locale=en
#THE DATA USED IS 2018 QUARTERLY DATA, NOT DATA FROM THE FIRST QUARTER OF 2019 AND WAS USED TO CREATE 2 CSV FILES 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#use pdf from honeybee survey to create a csv for yearly population data of bees

columns = ['state','colonies','max colonies','lost colonies','percent lost','added colonies','renovated colonies','percent renovated']
b18 = pd.read_csv('beespop2018.csv', usecols=columns)
#show columns and read yearly csv data

b18.drop('colonies', inplace=True, axis=1)
b18.drop('percent lost', inplace=True, axis=1)
b18.drop('added colonies', inplace=True, axis=1)
b18.drop('renovated colonies', inplace=True, axis=1)
b18.drop('percent renovated', inplace=True, axis=1)
#drop columns as needed


b18['max colonies'] = b18['max colonies'].astype('int')
b18['lost colonies'] = b18['lost colonies'].astype('int')
#turn columns into integers
b18['max colonies'] = b18['max colonies'].replace(np.nan, 0)
b18['lost colonies'] = b18['lost colonies'].replace(np.nan, 0)
#fill in zeros
groups1 = b18.groupby(['state'])['max colonies'].sum()
groups2 = b18.groupby(['state'])['lost colonies'].sum()
loss = (groups2/groups1)*100
#group to create percentages of loss for the total year (pdf was in quarter data)
losses18 = list(loss.items())
#create a list of groups

def Sort_Tuple(losses18):
    losses18.sort(key = lambda x: x[1])
    return losses18
#sort the data
print('\nORDERED BEE LOSSES BY STATE 2018', '\n', Sort_Tuple(losses18), '\n')
#show state order with percents of bee losses
bee18 = Sort_Tuple(losses18)
pd.DataFrame(bee18, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2018 TOTAL CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('2018TOTALSTATECCDLOSSES.png')
plt.show()
#create graph showing bee loss percentage from states from CCD

lowest_losses18 = bee18[0:3]
print('\n3 LOWEST LOSSES BY STATE IN 2018', '\n', lowest_losses18, '\n')

highest_losses18 = bee18[-3:]
print('\n3 HIGHEST LOSSES BY STATE IN 2018', '\n', highest_losses18, '\n')

top_low_18 = lowest_losses18 + highest_losses18
print('\nTOP AND LOW STATES 2018', top_low_18)
#show states with highest and lowest bee loss

pd.DataFrame(top_low_18, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2018 HIGHEST AND LOWEST STATE CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('HIGHESTANDLOWESTSTATECCDLOSSES2018.png')
plt.show()
#create graph of the top 3 and bottom 3 states by losses


#use the pdf to create a csv of the annual amount of colonies affected by CCD stressors
columns = ['varroamites','pests','diseases','pesticides','other','unknown']
c18 = pd.read_csv('ccd_2018_april_june.csv', usecols=columns)
#this shows april to june US data for colony stressors as there was not an annual amount 

print(c18)
#print out c15 data and copy over into lists
stressors = ['varroamites', 'pests', 'diseases', 'pesticides', 'other', 'unknown']
percentages = [56.4, 19.4, 11.6, 13.3, 14.7, 9.3]

#create a pie chart of the colony collapse stressors 
fig = plt.figure(figsize =(10, 7))
plt.pie(percentages, labels = stressors)
plt.title('% OF COLONIES AFFECTED BY STRESSORS IN APRIL-JUNE 2018')
plt.savefig('PIECHART2018STRESSORSFORUS.png')
plt.show()

