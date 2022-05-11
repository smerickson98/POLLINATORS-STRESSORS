#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 01:30:26 2022

@author: shannonerickson
"""

#THIS SCRIPT USES DATA FROM THE hcny0820.pdf FROM 
#https://usda.library.cornell.edu/concern/publications/rn301137d?locale=en
#THE DATA USED IS 2019 QUARTERLY DATA, NOT DATA FROM THE FIRST QUARTER OF 2020 AND WAS USED TO CREATE 2 CSV FILES 
#THIS DATA IS MISSING ITS APRIL TO JUNE DATA 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#use pdf from honeybee survey to create a csv for yearly population data of bees

columns = ['state','colonies','max colonies','lost colonies','percent lost','added colonies','renovated colonies','percent renovated']
b19 = pd.read_csv('beespop2019.csv', usecols=columns)
#show columns and read yearly csv data

b19.drop('colonies', inplace=True, axis=1)
b19.drop('percent lost', inplace=True, axis=1)
b19.drop('added colonies', inplace=True, axis=1)
b19.drop('renovated colonies', inplace=True, axis=1)
b19.drop('percent renovated', inplace=True, axis=1)
#drop columns as needed


b19['max colonies'] = b19['max colonies'].astype('int')
b19['lost colonies'] = b19['lost colonies'].astype('int')
#turn columns into integers
b19['max colonies'] = b19['max colonies'].replace(np.nan, 0)
b19['lost colonies'] = b19['lost colonies'].replace(np.nan, 0)
#fill in zeros
groups1 = b19.groupby(['state'])['max colonies'].sum()
groups2 = b19.groupby(['state'])['lost colonies'].sum()
loss = (groups2/groups1)*100
#group to create percentages of loss for the total year (pdf was in quarter data)
losses19 = list(loss.items())
#create a list of groups

def Sort_Tuple(losses19):
    losses19.sort(key = lambda x: x[1])
    return losses19
#sort the data
print('\nORDERED BEE LOSSES BY STATE 2019', '\n', Sort_Tuple(losses19), '\n')
#show state order with percents of bee losses
bee19 = Sort_Tuple(losses19)
pd.DataFrame(bee19, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2019 TOTAL CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('2019TOTALSTATECCDLOSSES.png')
plt.show()
#create graph showing bee loss percentage from states from CCD

lowest_losses19 = bee19[0:3]
print('\n3 LOWEST LOSSES BY STATE IN 2019', '\n', lowest_losses19, '\n')

highest_losses19 = bee19[-3:]
print('\n3 HIGHEST LOSSES BY STATE IN 2019', '\n', highest_losses19, '\n')

top_low_19 = lowest_losses19 + highest_losses19
print('\nTOP AND LOW STATES 2019', top_low_19)
#show states with highest and lowest bee loss

pd.DataFrame(top_low_19, columns=['States','Losses']).set_index('States').plot(kind='bar')
plt.title('2019 HIGHEST AND LOWEST STATE CCD LOSSES')
plt.xlabel('State')
plt.ylabel('% CCD Loss')
plt.tight_layout()
plt.savefig('HIGHESTANDLOWESTSTATECCDLOSSES2019.png')
plt.show()
#create graph of the top 3 and bottom 3 states by losses


#use the pdf to create a csv of the annual amount of colonies affected by CCD stressors
columns = ['varroamites','pests','diseases','pesticides','other','unknown']
c19 = pd.read_csv('ccd_2019_oct_dec.csv', usecols=columns)
#this shows april to june US data for colony stressors as there was not an annual amount 

print(c19)
#print out c15 data and copy over into lists
stressors = ['varroamites', 'pests', 'diseases', 'pesticides', 'other', 'unknown']
percentages = [45.7, 15, 5.4, 10.9,	8.6, 5.3]

#create a pie chart of the colony collapse stressors 
fig = plt.figure(figsize =(10, 7))
plt.pie(percentages, labels = stressors)
plt.title('% OF COLONIES AFFECTED BY STRESSORS IN OCT-DEC 2019')
plt.savefig('PIECHART2019STRESSORSFORUS.png')
plt.show()

