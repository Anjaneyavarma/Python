a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))
d = int(input("Enter D: "))

if (a>b) & (a>c):
    print("A is greater")
elif (b>c) & (b>d):
    print("B is greater")
elif (c>a) &(c>d):
    print("C is greater")
else:
    print("D is greater")




