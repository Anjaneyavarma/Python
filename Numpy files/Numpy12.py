#Numpy12.py
"""The L2 norm of a vector can be calculated in NumPy using the norm()
function with default parameters"""
from numpy import array
from numpy.linalg import norm
# define vector
a = array([1, 2, 3])
print(a)
# calculate norm
l2 = norm(a)
print(l2)
