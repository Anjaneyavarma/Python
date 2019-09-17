n = int(input("Enter a number"))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*", end=" ")
    print()


#
#list =[1,2,3,4,5,6,7,8,9,10]
#for i in list:
    #if(i%2==1):
        #print(i, end=" ")
        
#
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    lst2 = i + 2
    print(lst2, end=" ")
#
print()
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for x in list1:
    list2.append(x+2)
print(list2)        

#
print()
print(sum(list1)/len(list1))

#
print()
for i in range(21):
    if(i%2==0):
        print(i, end=" ")
#
print()
for i in range(0,21,2):
    print(i, end=" ")
