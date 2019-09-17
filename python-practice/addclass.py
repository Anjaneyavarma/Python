class A1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def square(self):
        print("Square is", self.x**2)
    def cube(self):
        print("cube is",self.y**3)
class B1(A1):
    def __init__(self,x,y):
        super().__init__(x,y)
    def addition(self):
        print("The addition of square and cube is",self.x**2 + self.y**3)
        
b = B1(int(input()), int(input()))
b.square()
b.cube()
b.addition()
