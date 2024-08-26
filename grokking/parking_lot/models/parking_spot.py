from abc import ABC
from grokking.parking_lot.models.vehicle import Vehicle


class ParkingSpot(ABC):
    def add_vehicle(self,vehicle:Vehicle):
        self.is_empty=False
        self.vehicle=vehicle
        return self.spot_number

    def remove_vehicle(self):
        self.is_empty=True
        self.vehicle=None
        print('Parking spot {self.spot_number} is now available!')
        return self.spot_number

class BikeWheelerParkingSpot(ParkingSpot):
    def __init__(self,spot_number, hour_charge=100, min_charge=1, is_empty=True):
        self.spot_number=spot_number
        self.is_empty=is_empty
        self.vehicle=None
        self.hour_charge=hour_charge
        self.min_charge=min_charge

class CarWheelerParkingSpot(ParkingSpot):
    def __init__(self,spot_number, hour_charge=200, min_charge=2, is_empty=True):
        self.spot_number=spot_number
        self.is_empty=is_empty
        self.vehicle=None
        self.hour_charge=hour_charge
        self.min_charge=min_charge

class BusWheelerParkingSpot(ParkingSpot):
    def __init__(self,spot_number, hour_charge=300, min_charge=3, is_empty=True):
        self.spot_number=spot_number
        self.is_empty=is_empty
        self.vehicle=None
        self.hour_charge=hour_charge
        self.min_charge=min_charge

