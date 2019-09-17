lst = ["michele","sara","cassie"]
name = input("Type name to check")
for letter in lst:
    if(name == letter):
        print("Student Admission is accepted")
    

#
string = "varma"
for i in string:
    print(i)

#
example =  " this     has          a       lot  of   spaces                          and   tabs  "
list1 = []
for i in example:
    list1 = example.split()
print(list1, end = ",")
print()


#
n = int(input("Enter a number"))
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()


        
#
a = int(input("Enter A"))
b = int(input("Enter B"))
def max(a,b):
    if(a>b):
        return "A is Max"
    else:
        return "B is Max"
print(max(a,b))
    
