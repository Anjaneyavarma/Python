#Panda8.py
"""How to get frequency counts of unique items of a series."""
#Calculte the frequency counts of each unique value ser.
import numpy as np
import pandas as pd
# Input
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

# Solution
print(ser.value_counts())
