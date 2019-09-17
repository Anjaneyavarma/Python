import pandas as pd
import numpy as np
df = pd.DataFrame({'col1':['apple','banana','orange']*3,
                   'col2':np.random.rand(9),
                   'col3':np.random.randint(0,15,9)})
df_grouped = df.groupby(['col1'])
print(df_grouped)
