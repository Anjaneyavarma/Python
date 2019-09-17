m = str(input())
y = 0
n = 0
while(y<len(m)):
    y+=1
    print(m[0:y])
while(n<len(m)):
    y-=1
    print(m[0:y])
    n+=1
