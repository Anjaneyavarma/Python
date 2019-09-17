from abc import ABCMeta, abstractmethod

class Jungle(metaclass = ABCMeta):
    def __init__(self,name = "unknown"):
        self.name = name
    def welcome(self):
        print("Hello %s, welcome  to jungle" % self.name)
    @abstractmethod
    def scarysound(self):
        pass
class Ratejungle(Jungle):
    def __init__(self):
        print("hi")
#overriding of super class method in subclass
    def scarysound(self):
        print('hello')
a = Ratejungle()
a.scarysound()
