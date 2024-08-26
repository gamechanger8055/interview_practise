from abc import ABC,abstractmethod

class State(ABC):
    @abstractmethod
    def select_product(self,product_id):
        pass

    @abstractmethod
    def insert_money(self,amount):
        pass

    @abstractmethod
    def dispense_product(self):
        pass