m = int(input())
if m>1:
    for i in range(2,m):
        if(m%i==0):
            print(m,"is not a prime number")
            break
    else:
        print(m,"Is a prime number")
