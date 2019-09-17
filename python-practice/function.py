def add():
    a = int(input("Enter a "))
    b = int(input("Enter b"))
    print(a+b)
add()
#
def oddlist():
    lst = [1,2,3,4,5,6]
    for i in lst:
        if(i%2==1):
            print(i, end=" ")
oddlist()
