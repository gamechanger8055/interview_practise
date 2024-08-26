from abc import ABC, abstractmethod
class Locker:
    def __init__(self,id,size):
        self.id=id
        self.size=size
        self.is_available=True
        self.allocated_user=None

    def allocate(self,user):
        self.is_available=False
        self.allocated_user=user

    def deallocate(self):
        self.is_available=True
        self.allocated_user=None

class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.locker=None

    def request_locker(self,lockerFacade):
        self.locker=lockerFacade.requestLocker(self)

    def release_locker(self,lockerFacade):
        self.locker=lockerFacade.requestLocker(self)

class AllocationStrategy(ABC):
    @abstractmethod
    def allocate(self,lockers):
        pass

class SizeBasedAllocationStrategy(AllocationStrategy):
    def __init__(self,size):
        self.size=size

    def allocate(self,lockers):
        for locker in lockers:
            if locker.is_available and locker.size==self.size:
                return locker
        return

class RoundRobinAllocationStrategy(AllocationStrategy):
    def allocate(self,lockers):
        for locker in lockers:
            if locker.is_available:
                return locker
        return

class LockerManager:
    def __init__(self,lockers,allocation_strategy):
        self.lockers=lockers
        self.allocation_strategy=allocation_strategy

    def add_locker(self,id,size):
        self.lockers.append(Locker(id,size))

    def findAvailableLocker(self):
        return self.allocation_strategy.allocate(self.lockers)


    def allocate_locker(self,user):
        locker=self.findAvailableLocker()
        if locker:
            locker.allocate(user)
            user.locker=locker
            return locker
        return

    def deallocate_locker(self,user):
        if user.locker:
            user.locker.deallocate()
            user.locker=None

class LockerFacade:
    def __init__(self,locker_manager):
        self.locker_manager=locker_manager

    def requestLocker(self,user):
        return self.locker_manager.allocate_locker(user)

    def releaseLocker(self,user):
        self.locker_manager.deallocate_locker(user)

lockers = [Locker(i, 'small') for i in range(5)] + [Locker(i + 5, 'large') for i in range(5)]
allocationStrategy = SizeBasedAllocationStrategy('small')
lockerManager = LockerManager(lockers, allocationStrategy)
lockerFacade = LockerFacade(lockerManager)

user1 = User(1, 'Alice')
user1.request_locker(lockerFacade)
print(f"User {user1.name} allocated locker: {user1.locker.id}")

user1.release_locker(lockerFacade)
print(f"User {user1.name} released locker.")

