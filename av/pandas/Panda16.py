import pandas as pd
mystring = 'dbc deb abed gade'
ser = pd.Series(list(mystring))
f = pd.Series(ser.value_counts())
leastf = f.dropna().index[-1]
print(ser.replace(' ',leastf))
print(''.join(ser.replace(' ',leastf)))
