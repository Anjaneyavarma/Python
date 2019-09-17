name  = str(input())
x = 0
for i in name:
    x+=1
    print(name[0:x])
  
for i in name:
    x-=1
    print(name[0:x])

    
#
x = int(input())
for i in range(0,5):
    for j in range(i):
        print("*", end=" ")
    print()  
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
