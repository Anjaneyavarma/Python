n = input("Enter a String")
s=''
for i in n:
    s = n[::-1]
if(n == s):
    print("Given String is palindrome")
else:
    print("Given string is not palindrome")
    
#
st = input("enter a string")
st1 = ''
for i in st:
    st1 = i+st1
if(st==st1):
    print("string is palindrome")
else:
    print("is not palindrome")
