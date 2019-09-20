import matplotlib.pyplot as plt
days = [4,2,3,7,6]
reading = [4,5,6,11,12]
running = [2,5,7,6,1]
cricket = [3,4,6,7,8]
tennis = [3,4,7,8,10]
plt.plot([],[],color='r',label='reading',linewidth=5)
plt.plot([],[],color='g',label='running',linewidth=5)
plt.plot([],[],color='k',label='cricket',linewidth=5)
plt.plot([],[],color='c',label='tennis',linewidth=5)
plt.stackplot(days,reading,running,cricket,tennis,colors=['r','g','k','c'])
plt.plot('x')
plt.plot('y')
plt.legend()
plt.show()
