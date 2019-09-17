n= int(input("Enter a number: "))
def fact(num):
    if(num==1):
        return num
    else:
        return num*fact(num-1)
if(n==0):
    print("Factorial of num is 1")
else:
    print(fact(n))
