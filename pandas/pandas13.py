import numpy as np
import pandas as pd
ser = pd.Series(list('abcdefghiklmnopqrstuvwyz'))
pos = [0,4,3,2]
print(ser.take(pos))
