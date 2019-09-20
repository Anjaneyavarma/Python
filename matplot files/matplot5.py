import matplotlib.pyplot as plt
average = [21,54,45,64,87,95,42,43,56,61,62,63,68,52,57,49,87,27,29,53]
bins = [0,5,10,15,20,25,30,35,45,50]
plt.hist(average,bins,histtype = 'bar', rwidth =  0.9)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.show()
