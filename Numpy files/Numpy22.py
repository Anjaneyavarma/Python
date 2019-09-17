#Numpy22.py
import numpy as np
x = np.array([[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9]], np.int32)
np.savetxt("test.txt", x)
#
np.savetxt("test2.txt", x, fmt="%2.3f", delimiter=",")
np.savetxt("test3.txt", x, fmt="%04d", delimiter=" :-) ")
#
y = np.loadtxt("test.txt")
print(y)
#
y = np.loadtxt("test2.txt", delimiter=",")
print(y)
#
y = np.loadtxt("test3.txt", delimiter=" :-) ", usecols=(0,2))
print(y)
#
def time2float_minutes(time):
    if type(time) == bytes:
        time = time.decode()
    t = time.split(":")
    minutes = float(t[0])*60 + float(t[1]) + float(t[2]) * 0.05 / 3
    return minutes

y = np.loadtxt("times_and_temperatures.txt",converters={ 0: time2float_minutes})
print(y)


#





