'''
Reqyirements:
1. elevator can go up and down between floors
2. we can press buttons on floor to stop elevators
3. inside elevators it has list of buttons for moving to that floor
4. elevator will fulfill the req in dirn to which its going and then reverse- scan and look via heap.


Elevator
-id
-current_floor
-state
-direction
-requests[]
--------------
add_reqyest()
changedirn()

FloorRequest
-floor
-direction
'''

from enum import Enum
from abc import ABC, abstractmethod
from threading import Lock
import unittest


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"


class ElevatorState(Enum):
    IDLE = "IDLE"
    MOVING = "MOVING"


class Elevator:
    def __init__(self, id, strategy):
        self.id = id
        self.current_floor = 0
        self.direction = Direction.UP
        self.state = ElevatorState.IDLE
        self.requests = []  # floor request
        self.lock = Lock()
        self.strategy = strategy

    def add_requests(self, request):
        with self.lock:
            self.requests.append(request)
            self.requests.sort(key=lambda x: x.target_floor)

    def move(self):
        self.process_requests()

    def step(self):
        self.move()
        print(f"Elevator {self.id} at floor {self.current_floor} moving {self.direction}")

    def process_requests(self):
        if not self.requests:
            self.state = ElevatorState.IDLE
            return
        if self.state == ElevatorState.IDLE:
            self.direction = Direction.UP if self.requests[0].target_floor > self.current_floor else Direction.DOWN
        next_request = self.strategy.get_next_request(self.requests, self.current_floor, self.direction)
        if next_request:
            self.current_floor = next_request.target_floor
            #self.direction = next_request.direction
            self.requests.remove(next_request)
        else:
            self.direction = Direction.DOWN if self.direction == Direction.UP else Direction.UP


class ElevatorRequest:
    def __init__(self, requested_floor, target_floor):
        self.req_floor = requested_floor
        self.target_floor = target_floor


class FloorRequest:
    def __init__(self, floor, direction):
        self.floor = floor
        self.direction = direction


class ElevatorController:
    def __init__(self,num_elevator,strategy):
        self.elevators=[Elevator(i,strategy) for i in range(num_elevator)]

    def add_request(self, request: ElevatorRequest):
        best_elevator = self.find_best_elevator(request)
        best_elevator.add_requests(request)

    def find_best_elevator(self, request: ElevatorRequest) -> Elevator:
        return min(self.elevators, key=lambda e: abs(e.current_floor - request.req_floor))

    def step(self):
        for elevator in self.elevators:
            elevator.step()

    def get_status(self):
        return [{"id": elevator.id, "current_floor": elevator.current_floor, "state": elevator.state.name, "direction": elevator.direction.name} for elevator in self.elevators]



class SchedulingAlgorithm(ABC):
    @abstractmethod
    def get_next_request(self, request, current_floor, direction):
        pass


class ScanSchedulingAlgorithm(SchedulingAlgorithm):

    def get_next_request(self, request, current_floor, direction):
        '''
        if moving Up, find smallest req>=curr_floor, if no req exists reverse dirn
        Down- find largest<=curr_floor,if no req reverse dirn
        '''
        if direction == Direction.UP:
            next_request = min([req for req in request if req.target_floor >= current_floor],
                               key=lambda x: x.target_floor, default=None)
            if next_request:
                return next_request
            return
        else:
            next_request = min([req for req in request if req.target_floor <= current_floor],
                               key=lambda x: x.target_floor, default=None)
            if next_request:
                return next_request
            return
        return


class LookSchedulingAlgorithm(SchedulingAlgorithm):
    def get_next_request(self, request, current_floor, direction):
        '''
        if moving Up, find smallest req>=curr_floor, if no req exists reverse dirn and look for largest req<=curr_floor
        Down- find largest<=curr_floor,if no req reverse dirn and look for smallest req >=curr
        '''
        if direction == Direction.UP:
            next_request = min([req for req in request if req.target_floor >= current_floor],
                               key=lambda x: x.target_floor, default=None)
            if next_request:
                return next_request
            return max(request, key=lambda x: x.target_floor, default=None)
        else:
            next_request = min([req for req in request if req.target_floor <= current_floor],
                               key=lambda x: x.target_floor, default=None)
            if next_request:
                return next_request
            return min(request, key=lambda x: x.target_floor, default=None)
        return


scan_strategy = LookSchedulingAlgorithm()
scheduler = ElevatorController(3, scan_strategy)
scheduler.add_request(ElevatorRequest(0, 5))
scheduler.add_request(ElevatorRequest(2, 8))
scheduler.add_request(ElevatorRequest(6, 1))

# for _ in range(2):
#     scheduler.step()
#     print(scheduler.get_status())


class TestElevatorSystem(unittest.TestCase):
    def setUp(self):
        self.scan_strategy = LookSchedulingAlgorithm()
        self.scheduler = ElevatorController(3, strategy=self.scan_strategy)

    def test_single_req(self):
        self.scheduler.add_request(ElevatorRequest(0,5))
        self.scheduler.step()
        status=self.scheduler.get_status()
        self.assertEqual(status[0]['current_floor'],5)
        self.assertEqual(status[0]['direction'], Direction.UP.name)

    def test_multiple_req(self):
        self.scheduler.add_request(ElevatorRequest(0, 5))
        self.scheduler.add_request(ElevatorRequest(5, 8))
        for _ in range(2):
            self.scheduler.step()
        status = self.scheduler.get_status()
        self.assertEqual(status[0]['current_floor'], 8)
        self.assertEqual(status[0]['direction'], Direction.UP.name)

if __name__ == "__main__":
    unittest.main()