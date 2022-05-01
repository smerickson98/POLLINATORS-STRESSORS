#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 22:32:35 2022

@author: shannonerickson
"""


#g02 script1

#step 1
# print('\n [whatever]')
# how to print something

#step 2
# string_variable = 'string' 
# connected_string = 'one' + 'two' + 'three'
# or [connect variables together for strings] - string = 'var1' + 'var2'
# sometimes it is string = var1+" "+var2

# write('string' + 'string' + 'string')
# numeric_variable = #

#open_files and write in them and close them
# filename = 'file.md'
# fh = open(filename, 'w')
#fh.write('# title\n')
# how to write lines in a new file
# fh.close()

#g03 script
#step 1 - create a list
# list = ['string1', 'string2']
#count list

# n = len(list)
# print('\nTHE LENGTH OF THE LIST IS:', len(list))

# joined_variable = ' ' .join(list[2:])
#join from the 3rd element on because the first element is 0

#append something1 to something2
# something2.apend('something1')

#split function
##split_list = list_to_split.split()

#extend by adding something2 to the end of something1
#something1.extend(something2[-3:])
#last 3 elements

#use sorted to put the list in alphabetical order
#sorted_list = sorted(list)

#g04
# for loops
# list = 1,3,5
#empty_list = []
#for x in list:
    #list2.append(x**2)
    #append squared variable to list 2

#list comprehension
#new_list = [x**2 for x in old_list]

#range()
#not sure what range does

#g05
#import json 
#allows complex data objects to be written out/read in a clear notation

#dictionary = {name, abbreviation, population}
#will separate the information 

#print( json.dumps(state_list,indent=4) )

# variable1 = "("+variable+")"
#not sure

#strip function - remove blank spaces
#stripped_line = line.strip()

#convert all to lower case
#lowercase_line = line.lower()

#g06
#define a new function
#def read_cashflow(filename):
    #payments = []
    #fh = open(filename)
   # for line in fh:
        #line = line.split()
        #new_pmt = t, amt
        #t = int('0'), amt = (float('1'))
        #payments.append(new_pmt)
        #return payments

#def npv(r, cashflow):
    #val = 0
    #for payments in cashflow:
        #r = [.05]
        #PV = ( t / ( ( 1 + r ) ** t ) )
        #PV.append(val)
        #return PV
        #close(fh)
        
#g07

#copy a py from repository 

#trim script

#splitter = None
#this agrument shows a default value of None

#add this argument to indicate that a file should be split into commas instead of spaces
#splitter=','

#opt.newton()

#g08

#import csv

#import scipy.optimize as opt

#create object
#fh = open('filename')
#reader = csv.Dictreader(fh)

#what does float do
#float()

#sum(list)
#return sum()
#add values in a list

#g09



















