#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:34:13 2022

@author: shannonerickson
"""
import pandas as pd
import numpy as np

#pd.set_option('display.max_rows', None, 'display.max_columns', None)


#low_pes = pd.read_csv('LowEstimate_AgPestUsebyCropGroup92to19.txt')

#print(low_pes)
                     
hp = open('LowEstimate_AgPestUsebyCropGroup92to19.txt', 'r')
#open txt file with pesticide data
#hp refers to high estimate pesticide use data
#'r' is the mode that will specify the way to open the file, r will read the file

#with open('LowEstimate_AgPestUsebyCropGroup92to19.txt') as p:
    #contents = p.read()
    #print(contents) 
    
#lines = hp.readlines()
#for line in lines:
    #print(line)

with hp as p:
    for line in p:
        print(line)
        
data_in = np.loadtxt('LowEstimate_AgPestUsebyCropGroup92to19.txt', dtype = int)

idx = np.where(np.logical_and(data_in[:,0]>2, data_in[:,0]<6))[0]

np.savetxt('xyz_filtered.txt', data_in[idx,:], fmt = '%d')


