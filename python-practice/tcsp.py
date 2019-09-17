s1 = str(input("Enter the first string"))
s2 = str(input("Enter the second string"))
s3 = str(input("Enter the third string"))

for i in range(len(s1)):
    if(s1[i] == 'a' or s1[i] == 'e' or s1[i] == 'i' or s1[i] == 'o' or s1[i] == 'u' or s1[i] == 'A' or s1[i] == 'E' or s1[i] == 'I' or s1[i] == 'O' or s1[i] == 'U'):
        s1 = s1.replace(s1[i],'"')
        print("s1: ", s1)

for i in range(len(s2)):
     if(s2[i] == 'a' or s2[i] == 'e' or s2[i] == 'i' or s2[i] == 'o' or s2[i] == 'u' or s2[i] == 'A' or s2[i] == 'E' or s2[i] == 'I' or s2[i] == 'O' or s2[i] == 'U'):
        continue
     else:
        s2 = s2.replace(s2[i],"*")
print("s2",s2)

print(s3.lower())
