#Panda10.py
"""How to convert a numpy array to a dataframe of given shape."""
#From ser, keep the top 2 most frequent items as it is and replace everything else as Other.
import numpy as np
import pandas as pd
# Input
ser = pd.Series(np.random.randint(1, 10, 35))

# Solution
df = pd.DataFrame(ser.values.reshape(7,5))
print(df)
