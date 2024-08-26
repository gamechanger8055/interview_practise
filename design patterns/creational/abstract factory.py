'''
he Abstract Factory pattern is a creational design pattern that provides an interface for creating families of related
 or dependent objects without specifying their concrete classes. This pattern allows you to create a suite of related
  objects without needing to specify their concrete classes, making it easier to introduce new types of objects without
    modifying existing code.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Color(ABC):
    @abstractmethod
    def fill(self):
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

class Red(Color):
    def fill(self):
        return "Filling with Red color"

class Green(Color):
    def fill(self):
        return "Filling with Green color"

class Blue(Color):
    def fill(self):
        return "Filling with Blue color"

class AbstractFactory(ABC):
    @abstractmethod
    def get_shape(self,shape_type):
        pass

    @abstractmethod
    def get_color(self,color_type):
        pass

class ShapeFactory(AbstractFactory):
    def get_shape(self, shape_type: str):
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "SQUARE":
            return Square()
        elif shape_type == "RECTANGLE":
            return Rectangle()
        return None

    def get_color(self, color_type: str):
        return None  # ShapeFactory doesn't implement get_color

class ColorFactory(AbstractFactory):
    def get_shape(self, shape_type: str):
        return None  # ColorFactory doesn't implement get_shape

    def get_color(self, color_type: str):
        if color_type == "RED":
            return Red()
        elif color_type == "GREEN":
            return Green()
        elif color_type == "BLUE":
            return Blue()
        return None

class FactoryProducer:
    @staticmethod
    def get_factory(choice):
        if choice=="SHAPE":
            return ShapeFactory()
        elif choice == "COLOR":
            return ColorFactory()
        return

if __name__ == "__main__":
    # Get shape factory
    shape_factory = FactoryProducer.get_factory("SHAPE")

    # Get an object of Shape Circle
    shape1 = shape_factory.get_shape("CIRCLE")
    print(shape1.draw())

    # Get an object of Shape Square
    shape2 = shape_factory.get_shape("SQUARE")
    print(shape2.draw())

    # Get an object of Shape Rectangle
    shape3 = shape_factory.get_shape("RECTANGLE")
    print(shape3.draw())

    # Get color factory
    color_factory = FactoryProducer.get_factory("COLOR")

    # Get an object of Color Red
    color1 = color_factory.get_color("RED")
    print(color1.fill())

    # Get an object of Color Green
    color2 = color_factory.get_color("GREEN")
    print(color2.fill())

    # Get an object of Color Blue
    color3 = color_factory.get_color("BLUE")
    print(color3.fill())
