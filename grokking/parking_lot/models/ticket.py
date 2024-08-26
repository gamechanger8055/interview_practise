import time
from grokking.parking_lot.models.parking_spot import *
from grokking.parking_lot.models.vehicle import *
class Ticket:
    def __init__(self,vehicle:Vehicle,price,parkingSpot:ParkingSpot):
        self.vehicle=vehicle
        self.price=price
        self.parkingSpot=parkingSpot
        self.entry_time=time.time()

    def generate_ticket(self):
        print(f'Entry time: {self.entry_time}')
        print(f'Spot No.: {self.parking_spot.spot_number}')
        print(f'Vehicle type: {self.vehicle.get_vehicle_type()}')
        print(f'Vehicle color: {self.vehicle.get_vehicle_color()}')



