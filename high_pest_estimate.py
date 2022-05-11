#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:56:04 2022

@author: shannonerickson
"""
#pesticide_stressors.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%A - Setting up the CSV file
hp = pd.read_csv('HighEstimate_AgPestUsebyCropGroup92to19.txt', sep = '\t')
#there are tabs in this csv file so the sep function will help us change it to , instead

hp.to_csv('HighEstimate_AgPestUsebyCropGroup92to19.csv', index = None)

columns = ['State_FIPS_code','State','Compound','Year','Units','Corn','Soybeans','Wheat','Cotton','Vegetables_and_fruit','Rice','Orchards_and_grapes','Alfalfa','Pasture_and_hay','Other_crops']
high_pest = pd.read_csv('HighEstimate_AgPestUsebyCropGroup92to19.csv', usecols=columns)

#if the block is empty, make it a zero
high_pest['Corn'] = high_pest['Corn'].replace(np.nan, 0)
high_pest['Soybeans'] = high_pest['Soybeans'].replace(np.nan, 0)
high_pest['Wheat'] = high_pest['Wheat'].replace(np.nan, 0)
high_pest['Cotton'] = high_pest['Cotton'].replace(np.nan, 0)
high_pest['Vegetables_and_fruit'] = high_pest['Vegetables_and_fruit'].replace(np.nan, 0)
high_pest['Rice'] = high_pest['Rice'].replace(np.nan, 0)
high_pest['Orchards_and_grapes'] = high_pest['Orchards_and_grapes'].replace(np.nan, 0)
high_pest['Alfalfa'] = high_pest['Alfalfa'].replace(np.nan, 0)
high_pest['Pasture_and_hay'] = high_pest['Pasture_and_hay'].replace(np.nan, 0)
high_pest['Other_crops'] = high_pest['Other_crops'].replace(np.nan, 0)

#add up the columns indicating pesticide use to get total amount in kg per area in a new column
high_pest['hp_kg'] = high_pest['Corn'] + high_pest['Soybeans'] + high_pest['Wheat'] + high_pest['Cotton'] + high_pest['Vegetables_and_fruit'] + high_pest['Rice'] + high_pest['Orchards_and_grapes'] + high_pest['Alfalfa'] + high_pest['Pasture_and_hay'] + high_pest['Other_crops']

#drop columns for type of crop and units since they are all in kg and use total crop columns and columns not used in next graph
high_pest.drop('Units', inplace=True, axis=1)
high_pest.drop('Corn', inplace=True, axis=1)
high_pest.drop('Soybeans', inplace=True, axis=1)
high_pest.drop('Wheat', inplace=True, axis=1)
high_pest.drop('Cotton', inplace=True, axis=1)
high_pest.drop('Vegetables_and_fruit', inplace=True, axis=1)
high_pest.drop('Rice', inplace=True, axis=1)
high_pest.drop('Orchards_and_grapes', inplace=True, axis=1)
high_pest.drop('Alfalfa', inplace=True, axis=1)
high_pest.drop('Pasture_and_hay', inplace=True, axis=1)
high_pest.drop('Other_crops', inplace=True, axis=1)
high_pest.drop('Compound', inplace=True, axis=1)
high_pest.drop('State_FIPS_code', inplace=True, axis=1)
#%% How pesticide use has changed over the years in the US
#add total pesticide use per state per year

groups = high_pest.groupby(['Year','State'])['hp_kg'].sum()/1e6

#we want the total pesticide amount to match up with each state/year pair so we groupby them and then sum the remaining columns

groups.unstack().plot()
#unstack the groupby data in order to plot the Years and Pesticide Amounts by State
plt.title('Change in Pesticide Use (High)')
plt.xlabel('Year')
plt.ylabel('Total pesticide use (kg in Millions)')
plt.ticklabel_format(style='plain')
plt.legend(fontsize=5, bbox_to_anchor=(1.02, 1), loc='upper right', borderaxespad=0)
plt.savefig('High_Pesticide.png')
plt.show()
#save and format graph of high estimated pesticide use over the years

bees = list(groups.items())
#create a list of groups

#%% 2015 BEE DATA
bee2015 = []
for y in bees:
    if 2015 in y[0]:
        bee2015.append(y)
#create empty list and fill with 2015 data
def Sort_Tuple(bee2015):
    bee2015.sort(key = lambda x: x[1])
    return bee2015
#sort 2015 data by pesticide use
print('\n2015 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS','\n', Sort_Tuple(bee2015), '\n')

bees2015 = Sort_Tuple(bee2015)
lowest_users15 = bees2015[0:3]
print('\n3 LOWEST PESTICIDE STATE USERS IN 2015', '\n', lowest_users15, '\n')

highest_users15 = bees2015[-3:]
print('\n3 HIGHEST PESTICIDE STATE USERS IN 2015', '\n', highest_users15, '\n')
#print and sort highest and lowest users (low to high)
#%% 2016 BEE DATA
bee2016 = []
for y in bees:
    if 2016 in y[0]:
        bee2016.append(y)
#repeat 2015 steps down the code to 2019
def Sort_Tuple(bee2016):
    bee2016.sort(key = lambda x: x[1])
    return bee2016

print('\n2016 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS','\n', Sort_Tuple(bee2016), '\n')

#print('\n2015 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS', Sort_Tuple(bee2015))

bees2016 = Sort_Tuple(bee2016)
lowest_users16 = bees2016[0:3]
print('\n3 LOWEST PESTICIDE STATE USERS IN 2016', '\n', lowest_users16, '\n')

highest_users16 = bees2016[-3:]
print('\n3 HIGHEST PESTICIDE STATE USERS IN 2016', '\n', highest_users16, '\n')

#%% 2017 BEE DATA
bee2017 = []
for y in bees:
    if 2017 in y[0]:
        bee2017.append(y)

def Sort_Tuple(bee2017):
    bee2017.sort(key = lambda x: x[1])
    return bee2017

print('\n2017 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS','\n', Sort_Tuple(bee2017), '\n')

#print('\n2015 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS', Sort_Tuple(bee2015))

bees2017 = Sort_Tuple(bee2017)
lowest_users17 = bees2017[0:3]
print('\n3 LOWEST PESTICIDE STATE USERS IN 2017', '\n', lowest_users17, '\n')

highest_users17 = bees2017[-3:]
print('\n3 HIGHEST PESTICIDE STATE USERS IN 2017', '\n', highest_users17, '\n')

#%% 2018 BEE DATA
bee2018 = []
for y in bees:
    if 2018 in y[0]:
        bee2018.append(y)

def Sort_Tuple(bee2018):
    bee2018.sort(key = lambda x: x[1])
    return bee2018

print('\n2018 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS','\n', Sort_Tuple(bee2018), '\n')

#print('\n2015 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS', Sort_Tuple(bee2015))

bees2018 = Sort_Tuple(bee2018)
lowest_users18 = bees2018[0:3]
print('\n3 LOWEST PESTICIDE STATE USERS IN 2018', '\n', lowest_users18, '\n')

highest_users18 = bees2018[-3:]
print('\n3 HIGHEST PESTICIDE STATE USERS IN 2018', '\n', highest_users18, '\n')

#%% 2019 BEE DATA
bee2019 = []
for y in bees:
    if 2019 in y[0]:
        bee2019.append(y)

def Sort_Tuple(bee2019):
    bee2019.sort(key = lambda x: x[1])
    return bee2019

print('\n2019 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS','\n', Sort_Tuple(bee2019), '\n')

#print('\n2015 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS', Sort_Tuple(bee2015))

bees2019 = Sort_Tuple(bee2019)
lowest_users19 = bees2019[0:3]
print('\n3 LOWEST PESTICIDE STATE USERS IN 2019', '\n', lowest_users19, '\n')

highest_users19 = bees2019[-3:]
print('\n3 HIGHEST PESTICIDE STATE USERS IN 2019', '\n', highest_users19, '\n')





