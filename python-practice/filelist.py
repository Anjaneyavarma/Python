lst = ["txt1.txt","txt2.txt","txt3.txt"]
for i in lst:
    f = open(i,"r")
    data = f.read()
    print(data)
