


class EnteranceGate:
    def __init__(self,parking_spot_manager_factory):
        self.parking_spot_manager_factory=parking_spot_manager_factory

    def findParkingSpot(self,vehicle_type,strategy="default"):
        parking_spot_manager=self.parking_spot_manager_factory.get_spot_manager(vehicle)


    def bookParkingSpot(self):
        pass

    def generateTicket(self):
        pass

    def assignParking(self):
        pass