import numpy as np
a =np.matrix([[1,2],[4,5]])
b = np.matrix([[1,2],[4,5]])
c = a*b
print(c)
#
x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
y = x[:2,1:3]
print(x[0,1])
print(y[0,0])
y[0,0] = 77
print(x[0,1])
