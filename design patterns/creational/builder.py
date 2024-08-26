'''
The Builder pattern is a creational design pattern that allows constructing complex objects step by step.
 Unlike other creational patterns, which often involve a single method for object creation, the Builder pattern provides
  a clear and readable way to construct objects, especially when the object needs to be created in multiple steps or involves
   several optional parameters.
'''

class Burger:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Burger: {self.type}"

class Drink:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Drink: {self.type}"

class Side:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Side: {self.type}"

class Meal:
    def __init__(self):
        self.burger=None
        self.side=None
        self.drink=None

    def set_burger(self, burger):
        self.burger = burger

    def set_drink(self, drink):
        self.drink = drink

    def set_side(self, side):
        self.side = side

    def __str__(self):
        return f"{self.burger}, {self.drink}, {self.side}"

from abc import ABC,abstractmethod

class MealBuilder(ABC):
    @abstractmethod
    def build_burger(self):
        pass

    @abstractmethod
    def build_drink(self):
        pass

    @abstractmethod
    def build_side(self):
        pass

    @abstractmethod
    def get_meal(self):
        pass

class VegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal=Meal()

    def build_burger(self):
        self.meal.set_burger(Burger("Veg Burger"))

    def build_drink(self):
        self.meal.set_burger(Drink("Orange Juice"))

    def build_side(self):
        self.meal.set_burger(Side("Salad"))

    def get_meal(self):
        return self.meal

class NonVegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal=Meal()

    def build_burger(self):
        self.meal.set_burger(Burger("Chicken Burger"))

    def build_drink(self):
        self.meal.set_burger(Drink("Pineapple Juice"))

    def build_side(self):
        self.meal.set_burger(Side("Fries"))

    def get_meal(self):
        return self.meal

class MealDirector:
    def __init__(self, builder):
        self._builder=builder

    def construct_meal(self):
        self._builder.build_burger()
        self._builder.build_drink()
        self._builder.build_side()
        return self._builder.get_meal()

if __name__ == "__main__":
    # Create a veg meal
    veg_builder = VegMealBuilder()
    director = MealDirector(veg_builder)
    veg_meal = director.construct_meal()
    print("Veg Meal:")
    print(veg_meal)

    print("\n")

    # Create a non-veg meal
    non_veg_builder = NonVegMealBuilder()
    director = MealDirector(non_veg_builder)
    non_veg_meal = director.construct_meal()
    print("Non-Veg Meal:")
    print(non_veg_meal)



