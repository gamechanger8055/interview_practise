from enum import Enum


class ElevatorDirection(Enum):
    UP=1
    DOWN=-1
    IDLE=0

class Request:
    def __init__(self,floor,direction=None):
        self.floor=floor
        self.direction=direction

class ElevatorCar:
    def __init__(self,id,total_floors):
        self.id=id
        self.current_floor=0
        self.direction=ElevatorDirection.IDLE
        self.requests=[]
        self.target_floor=set()
        self.total_floors=total_floors

    def add_request(self,request):
        self.requests.append((request.floor,request))

    def move(self):
        if self.requests:

