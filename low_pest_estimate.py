#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 13:09:12 2022

@author: shannonerickson
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lp = pd.read_csv('LowEstimate_AgPestUsebyCropGroup92to19.txt', sep = '\t')
#there are tabs in this csv file so the sep function will help us change it to , instead

lp.to_csv('LowEstimate_AgPestUsebyCropGroup92to19.csv', index = None)

columns = ['State_FIPS_code','State','Compound','Year','Units','Corn','Soybeans','Wheat','Cotton','Vegetables_and_fruit','Rice','Orchards_and_grapes','Alfalfa','Pasture_and_hay','Other_crops']
low_pest = pd.read_csv('LowEstimate_AgPestUsebyCropGroup92to19.csv', usecols=columns)

#if the block is empty, make it a zero
low_pest['Corn'] = low_pest['Corn'].replace(np.nan, 0)
low_pest['Soybeans'] = low_pest['Soybeans'].replace(np.nan, 0)
low_pest['Wheat'] = low_pest['Wheat'].replace(np.nan, 0)
low_pest['Cotton'] = low_pest['Cotton'].replace(np.nan, 0)
low_pest['Vegetables_and_fruit'] = low_pest['Vegetables_and_fruit'].replace(np.nan, 0)
low_pest['Rice'] = low_pest['Rice'].replace(np.nan, 0)
low_pest['Orchards_and_grapes'] = low_pest['Orchards_and_grapes'].replace(np.nan, 0)
low_pest['Alfalfa'] = low_pest['Alfalfa'].replace(np.nan, 0)
low_pest['Pasture_and_hay'] = low_pest['Pasture_and_hay'].replace(np.nan, 0)
low_pest['Other_crops'] = low_pest['Other_crops'].replace(np.nan, 0)

#add up the columns indicating pesticide use to get total amount in kg per area in a new column
low_pest['hp_kg'] = low_pest['Corn'] + low_pest['Soybeans'] + low_pest['Wheat'] + low_pest['Cotton'] + low_pest['Vegetables_and_fruit'] + low_pest['Rice'] + low_pest['Orchards_and_grapes'] + low_pest['Alfalfa'] + low_pest['Pasture_and_hay'] + low_pest['Other_crops']

#drop columns for type of crop and units since they are all in kg and use total crop columns and columns not used in next graph
low_pest.drop('Units', inplace=True, axis=1)
low_pest.drop('Corn', inplace=True, axis=1)
low_pest.drop('Soybeans', inplace=True, axis=1)
low_pest.drop('Wheat', inplace=True, axis=1)
low_pest.drop('Cotton', inplace=True, axis=1)
low_pest.drop('Vegetables_and_fruit', inplace=True, axis=1)
low_pest.drop('Rice', inplace=True, axis=1)
low_pest.drop('Orchards_and_grapes', inplace=True, axis=1)
low_pest.drop('Alfalfa', inplace=True, axis=1)
low_pest.drop('Pasture_and_hay', inplace=True, axis=1)
low_pest.drop('Other_crops', inplace=True, axis=1)
low_pest.drop('Compound', inplace=True, axis=1)
low_pest.drop('State_FIPS_code', inplace=True, axis=1)
#%% How pesticide use has changed over the years in the US
#add total pesticide use per state per year

groups2 = low_pest.groupby(['Year','State'])['hp_kg'].sum()/1e6
#we want the total pesticide amount to match up with each state/year pair so we groupby them and then sum the remaining columns

groups2.unstack().plot()
#unstack the groupby data in order to plot the Years and Pesticide Amounts by State
plt.title('Change in Pesticide Use (Low)')
plt.xlabel('Year')
plt.ylabel('Total pesticide use (kg in Millions)')
plt.ticklabel_format(style='plain')
plt.legend(fontsize=5, bbox_to_anchor=(1.02, 1), loc='upper right', borderaxespad=0)
plt.savefig('Low_Pesticide.png')
plt.show()
#format figure of low estimated pesticide use over the years


bees2 = list(groups2.items())
#create list of grouped data

#%% 2015 BEE DATA
bee2015 = []
for y in bees2:
    if 2015 in y[0]:
        bee2015.append(y)
#empty list to fill in 2015 data
def Sort_Tuple(bee2015):
    bee2015.sort(key = lambda x: x[1])
    return bee2015
#sort 2015 data
print('\n2015 LOWEST STATE PESTICIDE USERS TO HIGHEST STATE PESTICIDE USERS','\n', Sort_Tuple(bee2015), '\n')

bees2015 = Sort_Tuple(bee2015)
lowest_users15 = bees2015[0:3]
print('\n3 LOWEST PESTICIDE STATE USERS IN 2015', '\n', lowest_users15, '\n')

highest_users15 = bees2015[-3:]
print('\n3 HIGHEST PESTICIDE STATE USERS IN 2015', '\n', highest_users15, '\n')
#print highest and lowest users in order (low to high)
#%% 2016 BEE DATA
bee2016 = []
for y in bees2:
    if 2016 in y[0]:
        bee2016.append(y)
#repeat 2015 steps for rest of code to 2019
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
for y in bees2:
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
for y in bees2:
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
for y in bees2:
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



