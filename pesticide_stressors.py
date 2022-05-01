#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:56:04 2022

@author: shannonerickson
"""
#pesticide_stressors.py
import pandas as pd
import numpy as np
#%%A - Setting up the CSV file
hp = pd.read_csv('HighEstimate_AgPestUsebyCropGroup92to19.txt', sep = '\t')

#hp.columns = ['State_FIPS_code', 'State', 'Compound', 'Year', 'Units', 'Corn', 'Soybeans', 'Wheat', 'Cotton', 'Vegetables_and_fruit', 'Rice', 'Orchards_and_grapes', 'Alfalfa', 'Pasture_and_hay', 'Other_crops']

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

#drop columns for type of crop and units since they are all in kg and use total crop columns
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

#%% How pesticide use has changed over the years in the US
#add total pesticide use per state per year

#create new dataframe for change in pesticide use
US_high_pest = pd.DataFrame(high_pest)


#US_high_pest


#print(US_high_pest)
#print('\nCONDENSED HIGH PESTICIDE CSV')
#print('\n', high_pest)

#print(high_pest['Compound'])

#print(high_pest2)
#print(high_pest.head(2))
#print top 2 rows
#print(high_pest.tail(2))
#print bottom 2 rows
#high_pest is the dataframe
#df = pd.DataFrame('HighEstimate_AgPestUsebyCropGroup92to19.csv', columns = ['State_FIPS_code','State','Compound','Year','Units','Corn','Soybeans','Wheat','Cotton','Vegetables_and_fruit','Rice','Orchards_and_grapes','Alfalfa','Pasture_and_hay','Other_crops'])

#hp_total_units = high_pest['Corn'] + high_pest['Soybeans'] + high_pest['Wheat'] + high_pest['Cotton'] + high_pest['Vegetables_and_fruit'] + high_pest['Rice'] + high_pest['Orchards_and_grapes'] + high_pest['Alfalfa'] + high_pest['Pasture_and_hay'] + high_pest['Other_crops']
#high_pest.drop('Units', inplace=True, axis=1)
#high_pest.drop('Corn', inplace=True, axis=1)
#high_pest.drop('Soybeans', inplace=True, axis=1)
#high_pest.drop('Wheat', inplace=True, axis=1)
#high_pest.drop('Cotton', inplace=True, axis=1)
#high_pest.drop('Vegetables_and_fruit', inplace=True, axis=1)
#high_pest.drop('Rice', inplace=True, axis=1)
#high_pest.drop('Orchards_and_grapes', inplace=True, axis=1)
#high_pest.drop('Alfalfa', inplace=True, axis=1)
#high_pest.drop('Pasture_and_hay', inplace=True, axis=1)
#high_pest.drop('Other_crops', inplace=True, axis=1)

#print(high_pest['Year'])
#print(high_pest['Units'])
#print('\nCSV AFTER DROP/ADD', '\n', high_pest)
#this will differentiate the columns in the csv file

#example of how to print out a column
#print(high_pest['Year'])







#lp = pd.read_csv('LowEstimate_AgPestUsebyCropGroup92to19.txt')

#lp.to_csv('LowEstimate_AgPestUsebyCropGroup92to19.csv', index = None)

lp = pd.read_csv('LowEstimate_AgPestUsebyCropGroup92to19.txt', sep = '\t')

lp.to_csv('LowEstimate_AgPestUsebyCropGroup92to19.csv', index = None)


#