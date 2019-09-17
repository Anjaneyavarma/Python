name = str(input("Enter your name"))
for i in range(0,len(name)):
    s = name[i]
    if(i%2==0):
        print(s.upper(),end="")
    else:
        print(s.lower(),end="")
