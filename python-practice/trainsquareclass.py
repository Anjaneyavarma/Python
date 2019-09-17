class A2:
    def __init__(self,n):
        self.n = n
    def traingle(self):
        k = 2*self.n-2
        for i in range(self.n):
            for j in range(k):
                print(end=" ")
            k = k-1
            for j in range(i):
                print('*',end= " ")
            print()

class B2(A2):
    def __init__(self,n):
        super().__init__(n)
    def square(self):
        for i in range(self.n):
            if(i==0 or i==self.n-1):
                for j in range(self.n):
                    print("*",end = " ")
            elif(i>0 or i<self.n-1):
                for j in range(self.n):
                    if(j==0 or j==self.n-1):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")       
            print()
        
a = B2(5)
a.square()
a.traingle()
