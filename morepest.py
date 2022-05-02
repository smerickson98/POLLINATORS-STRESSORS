#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:04:52 2022

@author: shannonerickson
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%A - Setting up the CSV file

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

#values = ['1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']

values = [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
high_pest_15_19 = high_pest[high_pest.Year.isin(values) == False]
print(high_pest_15_19)
#drop excess years
#high_pest.sort_values('Year')
#print(high_pest)
#high_pest['Year'].drop('1992':'2014')

groups = high_pest_15_19.groupby(['Year','State'])['hp_kg'].sum()
#groups.sort_values('hp_kg')
groups.to_csv('groups.csv', index = None)

#string = groups.to_string()
#string = string.sort_values(hp_kg)
#print(string)
#print(groups.to_string())
#groups.unstack().plot(kind='bar')
#unstack the groupby data in order to plot the Years and Pesticide Amounts by State
#plt.title('Top 5 Pesticide States 2015 - 2019')
#plt.xlabel('Year')
#plt.ylabel('Total pesticide use (kg)')
#plt.show()

#plt.ticklabel_format(style='plain')
#plt.legend(fontsize=4)
#plt.legend(fontsize=5, bbox_to_anchor=(1.02, 1), loc='upper right', borderaxespad=0)
#plt.figure(dpi=300)
#plt.savefig('High_Pesticide.png')






