lst = ['malayalam','hahah','varma','sos']  
count = 0
for i in lst:
    str1 = i
    a = str1[::-1]
    if(a == str1):
        count+=1
print(count)
lst.sort(key = len)
print(lst)

            
     

