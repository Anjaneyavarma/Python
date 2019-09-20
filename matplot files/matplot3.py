import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
a = [5,7,12]
b = [11,15,16]
ab = [5,3,13]
cd = [4,14,8]
plt.plot(a,b,label = 'x cordinate',linewidth=4,color='red')
plt.plot(ab,cd,label = 'y cordinate',linewidth=4,color='green')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()
