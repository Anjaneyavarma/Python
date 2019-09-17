class A:
    def __init__(self,name="Unknown"):
        self.name = name
    def welcome(self):
        print("My name is: %s" % self.name)
class B(A):
    def __init__(self,name,feedback):
        super().__init__(name)
        self.feedback = feedback
    def details(self):
        print("thank u for the feedback %s" % self.name)
def main():
    m = B("varma",10)
    m.welcome()
    m.details()
if __name__ == '__main__':
    main()
