'''

E-commerce website. We want to implement a new feature which is basically a new way to deliver products.
Flow ->

Delivery person is requesting a locker. (He/she has the user and the package which can be sent along with the request).
System will assign a locker at random from the available ones.
This should be extensible in case we want to consider package attributes when assigning. Like weight, volume, etc
As part of response you will send the locker ID and a unique code. (to open it)
Delivery person will arrive, put in the code, system will validate it, and the package will be dropped.
System will also notify the customer about the locker ID and again a unique code.
Customer will arrive, put in the code, system will validate it, and the package will be picked up.
'''


from abc import ABC, abstractmethod
from typing import List, Optional
import random
import string

class Locker:
    def __init__(self, id: int, size: str):
        self.id = id
        self.size = size
        self.isOccupied = False
        self.package = None
        self.deliveryCode = None
        self.pickupCode = None

    def allocate(self, package):
        self.isOccupied = True
        self.package = package
        self.deliveryCode = self.generateCode()
        self.pickupCode = self.generateCode()

    def deallocate(self):
        self.isOccupied = False
        self.package = None
        self.deliveryCode = None
        self.pickupCode = None

    def generateCode(self) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def validateCode(self, code: str) -> bool:
        if self.deliveryCode == code:
            return True
        if self.pickupCode == code:
            return True
        return False

class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Package:
    def __init__(self, id: int, weight: float, volume: float, recipient: User):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.recipient = recipient

class DeliveryPerson:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def deliverPackage(self, lockerFacade, package: Package) -> Optional[Locker]:
        return lockerFacade.requestLocker(package)

class Customer(User):
    def pickUpPackage(self, lockerFacade, lockerId: int, code: str) -> bool:
        return lockerFacade.releaseLocker(lockerId, code)

class AllocationStrategy(ABC):
    @abstractmethod
    def allocateLocker(self, lockers: List[Locker], package: Package) -> Optional[Locker]:
        pass

class RandomAllocation(AllocationStrategy):
    def allocateLocker(self, lockers: List[Locker], package: Package) -> Optional[Locker]:
        availableLockers = [locker for locker in lockers if not locker.isOccupied]
        if availableLockers:
            return random.choice(availableLockers)
        return None

class LockerManager:
    def __init__(self, lockers: List[Locker], allocationStrategy: AllocationStrategy):
        self.lockers = lockers
        self.allocationStrategy = allocationStrategy

    def findAvailableLocker(self, package: Package) -> Optional[Locker]:
        return self.allocationStrategy.allocateLocker(self.lockers, package)

    def allocateLocker(self, package: Package) -> Optional[Locker]:
        locker = self.findAvailableLocker(package)
        if locker:
            locker.allocate(package)
            return locker
        return None

    def deallocateLocker(self, lockerId: int):
        for locker in self.lockers:
            if locker.id == lockerId:
                locker.deallocate()
                break

class LockerFacade:
    def __init__(self, lockerManager: LockerManager, notificationService):
        self.lockerManager = lockerManager
        self.notificationService = notificationService

    def requestLocker(self, package: Package) -> Optional[Locker]:
        locker = self.lockerManager.allocateLocker(package)
        if locker:
            self.notificationService.notifyCustomer(locker, package)
            return locker
        return None

    def releaseLocker(self, lockerId: int, code: str) -> bool:
        for locker in self.lockerManager.lockers:
            if locker.id == lockerId and locker.validateCode(code):
                self.lockerManager.deallocateLocker(lockerId)
                return True
        return False

class NotificationService:
    def notifyCustomer(self, locker: Locker, package: Package):
        print(f"Notification: Package {package.id} for {package.recipient.name} is in locker {locker.id}. Pickup code: {locker.pickupCode}")

# Example usage
lockers = [Locker(i, 'medium') for i in range(10)]
allocationStrategy = RandomAllocation()
lockerManager = LockerManager(lockers, allocationStrategy)
notificationService = NotificationService()
lockerFacade = LockerFacade(lockerManager, notificationService)

user = Customer(1, 'John Doe')
package = Package(1, 5.0, 10.0, user)
deliveryPerson = DeliveryPerson(1, 'Alice')

# Delivery person requests a locker
locker = deliveryPerson.deliverPackage(lockerFacade, package)
print(f"Locker ID: {locker.id}, Delivery Code: {locker.deliveryCode}")

# Customer picks up the package
isPickedUp = user.pickUpPackage(lockerFacade, locker.id, locker.pickupCode)
print(f"Package picked up: {isPickedUp}")
