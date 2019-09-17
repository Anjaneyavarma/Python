for i in range(1,4):
    y = "txt"+str(i)+".txt"
    f = open(str(y),"w+")
    x = "quiz"+str(i)+".py"
    file = open(str(x),"r")
    data = file.read()
    f.write(data)
f.close()
