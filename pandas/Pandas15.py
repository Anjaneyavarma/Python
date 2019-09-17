import numpy as np
import pandas as pd
ser = pd.Series(['how','are','you'])
print(pd.Series([len(i) for i in ser]))
#ser.map((lambda x: len(x)))
