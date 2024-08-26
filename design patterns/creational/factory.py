'''
The Factory Method pattern is a creational design pattern that provides an interface for creating objects in a superclass,
 but allows subclasses to alter the type of objects that will be created. This pattern promotes loose coupling by eliminating
  the need to bind application-specific classes into your code. The code interacts solely with the resultant interface or
   abstract class, making the code more flexible and reusable.


   The Factory Method pattern is perfect for scenarios where you need to create instances
    of different classes that share a common interface.
'''

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()

class SquareFactory(ShapeFactory):
    def create_shape(self):
        return Square()

class RectangleFactory(ShapeFactory):
    def create_shape(self):
        return Rectangle()

def client_code(shape_factory: ShapeFactory):
    shape = shape_factory.create_shape()
    print(shape.draw())

if __name__ == "__main__":
    print("App: Using CircleFactory to create a Circle.")
    client_code(CircleFactory())

    print("\nApp: Using SquareFactory to create a Square.")
    client_code(SquareFactory())

    print("\nApp: Using RectangleFactory to create a Rectangle.")
    client_code(RectangleFactory())