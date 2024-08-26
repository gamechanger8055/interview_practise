from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile