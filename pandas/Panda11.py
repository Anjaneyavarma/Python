#Panda11.py
"""How to find the positions of numbers that are multiples of 3 from a series"""
#Find the positions of numbers that are multiples of 3 from ser
import numpy as np
import pandas as pd
# creating list 
list =[1, 0, 12, 1, 0, 4, 22, 0, 3, 9] 
  
# creating series 
series = pd.Series(list) 
  
# calling .nonzero() method 
result = series.to_numpy().nonzero()
  
# display 
print(result) 
  
# retrieving values using iloc method 
values = series.iloc[result] 
  
# display 
print(values) 
