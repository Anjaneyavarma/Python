import numpy as pd
import pandas as pd
ser = pd.Series(['how','are','you'])
#print(ser.map(lambda x:x.title()))
print(pd.Series([i.title() for i in ser]))
