Locker Management System

- Users can sign up and log in
- Admins can add/remove users
- User can reserve and release lockers
- Users can view available lockers.
- Admin can view all lockers and their status
- Admin can do crud of lockers.
- users can reserve lockers for specific duration
- users can release before duration

Locker
- id
- size
- allocated_to
- is_occupied

methods:
- allocate()
- deallocate()

User
- id
- name
- locker

methods:
- requestLocker()
- releaseLocker()

LockerManager
- lockers
- allocation_strategy

methods
- findAvailableLocker()
- allocateLocker()
- deallocateLocker()
