a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
count = 0
for i in range(a,b):
    if(i%c==0):
        print(i)
        count+=1
print(count)
     
