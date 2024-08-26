from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    def clone(self):
        pass


class ConcretePrototype1(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype2(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


# Client code
if __name__ == "__main__":
    prototype1 = ConcretePrototype1("Object1")
    prototype2 = ConcretePrototype2("Object2")

    # Clone the prototypes
    clone1 = prototype1.clone()
    clone2 = prototype2.clone()

    print(f"Prototype1 value: {prototype1.value}")
    print(f"Clone1 value: {clone1.value}")
    print(f"Prototype2 value: {prototype2.value}")
    print(f"Clone2 value: {clone2.value}")

    # Modify the cloned object
    clone1.value = "Modified Object1"
    print(f"Modified Clone1 value: {clone1.value}")
    print(f"Original Prototype1 value after modification: {prototype1.value}")
