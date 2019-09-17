n = input("Enter a String")
for i in n:
    s = n[::-1]
if(n == s):
    print("Given String is palindrome")
else:
    print("Given string is not palindrome")
