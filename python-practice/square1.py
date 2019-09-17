def shape():
    for i in range(1,6):
        if(i==1):
            for j in range(1,6):
                print("*", end = " ")
        else:
            print("*# # # #*", end=" ")
        print()
        if(i == 5):
            for j in range(1,6):
                print("*", end= " ")
shape()
