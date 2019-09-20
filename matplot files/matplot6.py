import matplotlib.pyplot as plt
a = [2,4,6,8,10,12,14,16]
b = [1,1.5,2,2.5,3,3.5,4,4.5]
plt.scatter(a,b,label='high income low saving',color='r')
plt.xlabel('saving*100')
plt.ylabel('income*100')
plt.legend()
plt.show()
