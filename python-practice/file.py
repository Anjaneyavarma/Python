
#print(f.readlines())
m = open("hai.txt","w")
m.write("3 hai this anjaneya")
m.close()

f = open("hai.txt","r")
for i in f:
    print(i)
f.close()
