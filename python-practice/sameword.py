try:
    f = open("para1.txt","r")
    w = f.read()
except IOError:
    print("para1.txt file not found please make sure file in the dir")
else:
    print(w)

#
try:
    f1 = open("para.txt","r")
    x = f1.read()
finally:
    print("no such file in dir or it can't read file")
    
