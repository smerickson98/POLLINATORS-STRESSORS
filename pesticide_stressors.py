#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:56:04 2022

@author: shannonerickson
"""

import pandas as pd

hp = pd.read_csv('HighEstimate_AgPestUsebyCropGroup92to19.txt', sep = '\t')

#hp.columns = ['State_FIPS_code', 'State', 'Compound', 'Year', 'Units', 'Corn', 'Soybeans', 'Wheat', 'Cotton', 'Vegetables_and_fruit', 'Rice', 'Orchards_and_grapes', 'Alfalfa', 'Pasture_and_hay', 'Other_crops']

hp.to_csv('HighEstimate_AgPestUsebyCropGroup92to19.csv', index = None)

#lp = pd.read_csv('LowEstimate_AgPestUsebyCropGroup92to19.txt')

#lp.to_csv('LowEstimate_AgPestUsebyCropGroup92to19.csv', index = None)

lp = pd.read_csv('LowEstimate_AgPestUsebyCropGroup92to19.txt', sep = '\t')

lp.to_csv('LowEstimate_AgPestUsebyCropGroup92to19.csv', index = None)

