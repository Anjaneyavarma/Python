#Numpy23.py
from datetimerange import trange
import random

fh = open("times_and_temperatures.txt", "w")

for time in trange((6, 0, 0), (23, 0, 0), (0, 1, 30) ):
    random_number = random.randint(100, 250) / 10
    lst = time + (random_number,)
    output = "{:02d}:{:02d}:{:02d} {:4.1f}\n".format(*lst)
    fh.write(output)

