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
#totals = groups['hp_kg'].sum()
#print(groups.to_string())
#we want the total pesticide amount to match up with each state/year pair so we groupby them and then sum the remaining columns
#print the string to compare to the graph we will produce to make sure it is correct

#from wilcoxen
#groups = data.groupby(['State_FIPS_code', 'State', 'Year'])
#totals = groups['hp_kg'].sum()

#fig1=
groups.unstack().plot()
#unstack the groupby data in order to plot the Years and Pesticide Amounts by State
plt.title('Change in Pesticide Use (High)')
plt.xlabel('Year')
plt.ylabel('Total pesticide use (kg in Millions)')
plt.ticklabel_format(style='plain')
#plt.legend(fontsize=4)
plt.legend(fontsize=5, bbox_to_anchor=(1.02, 1), loc='upper right', borderaxespad=0)
#plt.figure(dpi=300)
plt.savefig('High_Pesticide.png')
plt.show()
#fig1.savefig('High Pesticide.png')
#format the graph with labels and styles

#%% REPEAT FOR LOW PESTICIDE USE GRAPH

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
#totals = groups['hp_kg'].sum()
#print(groups2.to_string())
#we want the total pesticide amount to match up with each state/year pair so we groupby them and then sum the remaining columns
#print the string to compare to the graph we will produce to make sure it is correct

#from wilcoxen
#groups = data.groupby(['State_FIPS_code', 'State', 'Year'])
#totals = groups['hp_kg'].sum()

#fig2=
groups2.unstack().plot()
#unstack the groupby data in order to plot the Years and Pesticide Amounts by State
plt.title('Change in Pesticide Use (Low)')
plt.xlabel('Year')
plt.ylabel('Total pesticide use (kg in Millions)')
plt.ticklabel_format(style='plain')
#plt.legend(fontsize=4)
plt.legend(fontsize=5, bbox_to_anchor=(1.02, 1), loc='upper right', borderaxespad=0)
#plt.figure(dpi=300)
plt.savefig('Low_Pesticide.png')
plt.show()
#fig2.savefig('Low Pesticide.png')
#format the graph with labels and styles


