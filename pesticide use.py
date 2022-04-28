#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:34:13 2022

@author: shannonerickson
"""

hp = open('HighEstimate_AgPestUsebyCropGroup92to19.txt', 'r')
#open txt file with pesticide data
#hp refers to high estimate pesticide use data
#'r' is the mode that will specify the way to open the file, r will read the file

#with open('HighEstimate_AgPestUsebyCropGroup92to19.txt') as p:
    #contents = p.read()
    #print(contents) 
    
with hp as p:
    for line in p:
        print(line)
        
        
   
    

