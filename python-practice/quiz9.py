name = str(input("Enter a string: "))
count=0
s = 0
for i in name:
    if(i == " "):
        s+=1    
    else:
        count+=1
print("The number characters in a string is: ",count)
