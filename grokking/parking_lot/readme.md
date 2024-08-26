Requirements
- Parking lot should have multiple floors
- Each floor has slot dedicated for car,bike,truck
- It has entry and exit gate.
- In entry gate, vehicle is given slot and ticket is generated.
- Exit gate, slot is free and payment is done.

Db schema Design

Slots
- id
- floor id
- is_occupied
- slot_type(bike,car)


Floor
- id
- capacity

Vehicle
- id
- reg
- color
- rate/hour


Gatelog
- id
- gatetype
- vehicle
- datetime

ParkingLot
- id
- name
- location


Ticket
- id
- slot id
- entry time
- exit time
- vehicle_type
- cost
- payment_status(paid,unpaid)

Payment
- id
- ticket id
- payment mode

User
- id
- name
- email
- phone