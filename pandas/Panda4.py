#Panda4.py
#How to assign name to the series’ index
import numpy as np
import pandas as pd
# Input

ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

# Solution
ser.name = 'alphabets'
#print(ser)
print(ser.head())
