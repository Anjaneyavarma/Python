#Panda7.py
"""How to get the minimum, 25th percentile,
median, 75th, and max of a numeric series
Compute the minimum, 25th percentile, median, 75th, and maximum of ser."""
import numpy as np
import pandas as pd
# Input
state = np.random.RandomState(100)
ser = pd.Series(state.normal(10, 5, 25))

# Solution
print(np.percentile(ser, q=[0, 25, 50, 75, 100]))
