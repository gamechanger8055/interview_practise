'''
Requirements:
1. System support renting of car,motorcycle etc.
2. Vehicle should have reg, km driven etc, price.(strategy)
3. user should get a rented car for specific days he mentioned.
4. Inventory should be maintained for all vehicles

class design

Vehicle
-id
-type
-model
-km run
-is_Available

VehicleRental
-vehicles[]
'''

from enum import Enum

class VehicleType:
    CAR,BIKE="CAR","BIKE"

class AvailabilityStatus:
    AVAILABLE,BOOKED,UNDER_MAINTENANCE="AVAILABLE","BOOKED","UNDER_MAINTENANCE"

class VehicleRentalSystem:
    def __init__(self):
        self.stores=[]

    def add_stores(self,store):
        self.stores.append(store)

class Store:
    def __init__(self,name,location):
        self.name=name
        self.location=location


class Vehicle:
    def __init__(self,model,mileage):
        self.model=model
        self.mileage=mileage
        self.availabe=True

    def reserver(self):
        self.availabe=False

    def unreserve(self):
        self.availabe = True


class Car(Vehicle):
    def __init__(self,model,mileage):
        super().__init__(model,mileage)
        self.type=VehicleType.CAR

class Bike(Vehicle):
    def __init__(self,model,mileage):
        super().__init__(model,mileage)
        self.type=VehicleType.BIKE

class VehicleManagemntSystem:
    def __init__(self):
        self.vehicles=[]
    def add_vehicle(self,vehicle):
        pass
    def remove_vehicle(self):
        pass

class VehicleLog:
    def __init__(self,id, type, description, creation_date):
        self.id=id
        self.type=type
        self.desc=description
        self.created_at=creation_date

    def search_vehicle(self,type):
        pass

class Registration:
    pass

from abc import ABC


class Search(ABC):
    def search_by_type(self, type):
        None

    def search_by_model(self, model):
        None


class VehicleInventorySearch(Search):
    def __init__(self):
        self.__vehicle_types = {}
        self.__vehicle_models = {}

    def search_by_type(self, query):
        # return all vehicles of the given type.
        return self.__vehicle_types.get(query)

    def search_by_model(self, query):
        # return all vehicles of the given model.
        return self.__vehicle_models.get(query)



