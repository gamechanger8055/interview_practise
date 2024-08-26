from abc import ABC
from grokking.parking_lot.models.VehiicleType import VehicleType

class Vehicle(ABC):

    def __init__(self,color,reg_no,vehicle_type):
        self.reg_no = reg_no
        self.color = color
        self.vehicle_type = vehicle_type

    def create_vehicle(self, color, registration_no, vehicle_type):
        if vehicle_type == VehicleType.BIKE:
            return Bike(color, registration_no)
        if vehicle_type == VehicleType.CAR:
            return Car(color, registration_no)
        if vehicle_type == VehicleType.BUS:
            return Bus(color, registration_no)

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_vehicle_color(self):
        return self.color

    def get_vehicle_registration_no(self):
        return self.reg_no


class Bike(Vehicle):
    def __init__(self, color=None, reg_no=None, vehicle_type=VehicleType.BIKE):
        super().__init__(color, reg_no, vehicle_type)
        # self.vehicle_type=vehicle_type
        # self.color=color
        # self.reg_no=reg_no

class Car(Vehicle):
    def __init__(self, color=None, reg_no=None, vehicle_type=VehicleType.CAR):
        super().__init__(color, reg_no, vehicle_type)
        # self.vehicle_type=vehicle_type
        # self.color=color
        # self.reg_no=reg_no

class Bus(Vehicle):
    def __init__(self, color=None, reg_no=None, vehicle_type=VehicleType.BUS):
        super().__init__(color, reg_no, vehicle_type)
        # self.vehicle_type=vehicle_type
        # self.color=color
        # self.reg_no=reg_no



