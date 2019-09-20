import matplotlib.pyplot as plt
plt.bar([0.24,1.20,2.24,3.20,4.22],[40,30,60,70,10] , label ='car', width = 0.5)
plt.bar([0.65,1.65,2.55,3.85,4.85],[70,10,20,40,30] , label ='bus', width = 0.5)
plt.legend()
plt.xlabel('days')
plt.ylabel('Distance (kms)')
plt.show()
