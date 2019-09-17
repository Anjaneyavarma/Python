class Myclass:
    def __init__(self,name="Bhargav",age=22,weight=75):
        self.a = name
        self.b = age
        self.c = weight
    def welcome(self):
        print("My name is: ",self.a)
        print("Age is: ", self.b)
        print("Weight: ", self.c)
m = Myclass("varma",22,69)
m.welcome()
n = Myclass()
n.welcome()
