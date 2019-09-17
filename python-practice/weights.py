import numpy as np
NumPersons = np.array([[100,175,210],[90,160,150],[200,50,100],[120,0,310]])
price_per_100g = np.array([20.98,30.90,10.99])
price_incent = np.dot(NumPersons,price_per_100g)
price_in_rupees = price_incent/np.array([100,100,100,100])
print(price_in_rupees)
