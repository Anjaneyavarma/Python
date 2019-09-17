class Jungle:
    def __init__(self,name="Bhargav"):
        self.name = name
    def welcome(self):
        print("My name is: ", self.name)
def main():
    j = Jungle("varma")
    j.welcome()

    k = Jungle()
    k.welcome()
if __name__ == "__main__":
    main()
