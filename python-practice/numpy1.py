import numpy as np
lst = [1,2,3,4,5,6,7,8,9]
mean = np.mean(lst)
print(mean)

#
a = np.array([[1,2,3],
             [4,5,6]])
b = np.array([[1,2,3],
              [4,5,6]])
print(a)
print(type(a))
print(a.ndim)
print(a.shape)
print(a.size)
c = np.add(a,b)
print(c)
d = np.subtract(a,b)
print(d)
e = np.multiply(a,b)
print(e)
print(a*b)
g = np.average(a)
print(g)
