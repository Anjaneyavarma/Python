#Numpy11.py
"""The L1 norm of a vector can be calculated in NumPy using the norm()
function with aparameter to specify the norm order, in this case 1."""
from numpy import array
from numpy.linalg import norm
# define vector
a = array([1, 2, 3])
print(a)
# calculate norm
l1 = norm(a, 1)
print(l1)
