#Panda12.py
"""How to find the positions of numbers that are multiples of 3 from a series"""
#Find the positions of numbers that are multiples of 3 from ser
import numpy as np
import pandas as pd
# creating list 
df = pd.read_csv("Salaries.csv")
print(df.head())  #prints first 5 records if no parameters given
#how to print firts 10 records write code here
#Check a particular column type
print(df['salary'].dtype)
#Check types for all the columns
print(df.dtypes)




  

