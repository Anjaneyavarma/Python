from abc import ABCMeta, abstractmethod

class Jungle(metaclass = ABCMeta):
    def __init__(self,name = "unknown"):
        self.name = name
    def welcome(self):
        print("Hello %s, welcome  to jungle" % self.name)
    @abstractmethod
    def scarysound(self):
        pass
