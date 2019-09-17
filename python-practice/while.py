n = int(input())
m = 0
while(m<11):
    m+=1
    print(n,"*",m,"=",n*m)
    
    

#
m = str(input())
y = 0
while(y<=len(m)):
    y+=1
    print(m[0:y])

while(y<len(m)):
    y-=1
    print(m[0:y])
