import matplotlib.pyplot as plt
import pandas as pd
#import data
df = pd.read_csv('diamonds.csv')\
#plot
fig, axes = plt.subplots(1,5,figsize=(10,2.5),dpi=100,sharex=True,sharey=True)
colors=['tab:red','tab:blue','tab:green','tab:pink','tab:olive']
for i, (ax,cut) in enumerate(zip(axes.flatten(), df.cut.unique())):
    x = df.loc[df.cut==cut, 'depth']
    ax.hist(x, alpha=0.5, bins=100, density=True, stacked=True, label=str(cut), color=colors[i])
    ax.set_title(cut)
plt.suptitle('Probability Histogram of daimond Depth',y=1.05,size=16)
ax.set_xlim(30,70)
ax.set_ylim(0,1)
plt.tight_layout()
plt.show()
