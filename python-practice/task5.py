lst = [1,2]
x = len(lst)
if x>5:
    del lst[5:]
    print(lst)
for i in range(x,5):
    lst.append(i)
print(lst)


#
n = int(input("Enter the number"))
j = 1
for i in range(i,n):
    for j in range(i):
        print("*")
    print()
        
#
lst = [1,2,3,4]
for x in lst:
    print(x, end = " ")
    
 