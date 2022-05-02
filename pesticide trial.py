#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 16:04:36 2022

@author: shannonerickson
"""

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
from pandas import DataFrame
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
high_pest.drop('Compound', inplace=True, axis=1)
#%% How pesticide use has changed over the years in the US
#add total pesticide use per state per year

#create new dataframe for change in pesticide use
#US_high_pest = pd.DataFrame(high_pest)
#fill in blanks with zeros
#US_high_pest = US_high_pest.fillna(0)

#group the States and Years together
#high_pest.set_index('Year', inplace=True)
#high_pest.groupby('State')['hp_kg'].sum().plot(legend=True)

#high_pest.groupby(['State_FIPS_code','State', 'Year'])['hp_kg'].sum().plot(legend=True)

groups = high_pest.groupby(['Year','State'])['hp_kg'].sum()
#totals = groups['hp_kg'].sum()
print(groups.to_string())
#new = groups.append(totals)

#from wilcoxen
#groups = high_pest.groupby(['State_FIPS_code', 'State', 'Year']).sum()
#groups.to_csv('groups.csv', index = None)
#columns = ['State_FIPS_code','State','Year','hp_kg']
#US_high_pest = pd.read_csv('groups.csv')

#totals = groups['hp_kg'].sum()


#groups = high_pest.groupby(['State_FIPS_code','State', 'Year'])
#totals = groups['hp_kg'].sum()
#high_pest.groupby('Year')['hp_kg'].sum().plot(legend=True)
#print(totals)
groups.unstack().plot()
#plt.plot(high_pest['Year'], totals)
plt.title('Change in Pesticide Use (High)')
plt.xlabel('Year')
plt.ylabel('Total pesticide use (kg)')
plt.ticklabel_format(style='plain')
#plt.ticklabel_format(useOffset=False)
plt.show()

#print(totals)
#combine the 'hp_kg' for different compounds into one total for the State/Year groups

#from wilcoxen
#groups = high_pest.groupby(['State_FIPS_code', 'State', 'Year'])
#totals = groups['hp_kg'].sum()

#totals.to_csv('totals.csv', index = None)

#columns = ['hp_kg']
#US_high_pest = pd.read_csv('totals.csv', usecols=columns)

#US_high_pest['hp_kg'] = US_high_pest['hp_kg'].replace(np.nan, 0)

#totals.drop('State_FIPS_code', inplace=True, axis=1)
#totals = totals.unstack(level=0)

#totals.to_csv('totals.csv', index = None)

#columns = ['hp_kg']
#us_hp = pd.read_csv('totals.csv', header='hp_kg')

#print(us_hp['tot_hp_kg'])


#US_high_pest = pd.DataFrame(totals)

#print(US_high_pest)

#US_high_pest.rename(columns = {'hp_kg' : 'tot_hp_kg'})

#print(US_high_pest['State'])

#plt.plot('Year','State_FIPS_code')
#plt.title('Change in Pesticide Use (High)')
#plt.xlabel('Year')
#plt.ylabel('Total pesticide use (kg)')
#plt.show()

#groups.to_frame()
#totals.columns = ["State_FIPS_code", "State", "Year", "total_hp_kg"]
#print(groups['State'])

#import matplotlib.pyplot as plt

#plt.plot(xAxis,yAxis)
#plt.title('title name')
#plt.xlabel('xAxis name')
#plt.ylabel('yAxis name')
#plt.show()

#print(state_totals)
#print(US_high_pest)
#print(US_high_pest['state_totals'])
#print(US_high_pest['hp_kg'].sum())
#US_high_pest.drop('Compound', inplace=True, axis=1)

#if US_high_pest == US_high_pest.duplicated(subset=['State', 'Year']):
    #hp_kg_tot=['hp_kg'].sum()

#print(hp_kg_tot)
#US_high_pest.groupby('Year', as_index=False)
#print(US_high_pest.head(50))
#US_high_pest.set_index('Year', inplace=True)
#US_high_pest.groupby('State_FIPS_code', as_index=False).agg(State_FIPS_code=("State_FIPS_code", "first"),
                                           #State=("State", "first"),
                                           #Year=("Year", "first"),
                                           #hp_kg_tot=("hp_kg", "sum"))







#if US_high_pest['State'] == US_high_pest['State'] and US_high_pest['Year'] == US_high_pest['Year']:
    #print(US_high_pest)
#US_high_pest['tot_hp_hg'] = US_high_pest.groupby('State_FIPS_code')
#when year, fips, and year are all the same add up the ['hp_kg' column]

#print(US_high_pest)
#If year and state and FIPS are the same - add up the hp_kg
#US_high_pest = US_high_pest.fillna(0)

#US_high_pest.set_index('Year', 'State', inplace=True)
#US_high_pest['tot_hp_kg'] = []


#for x in US_high_pest:
    #if US_high_pest['State'] == US_high_pest['State'] and US_high_pest['Year'] == US_high_pest['Year'] and US_high_pest['State_FIPS_code'] == US_high_pest['State_FIPS_code']:
        #sum(high_pest['hp_kg'])
        
    
                        

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