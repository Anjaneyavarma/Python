f = open("text2.txt","w+")
for i in range(1,4):
    x = "quiz"+str(i)+".py"
    file = open(str(x),"r")
    data = file.read()
    f.write("*************")
    f.write(" ")
    f.write(data)
f.close()
