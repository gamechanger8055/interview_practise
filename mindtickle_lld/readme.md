Restaurant Management System


Requirements:
- Users can reserve/cancel a table.
- Admin will allocate the available table to user
- User can order food/drinks.
- User can pay bill.
- Order should be recived by kitchen
- Once order is ready, notification sent so that food can be served.
- Admin can change/crud on menu

Entities

Admin
- id
- name
- mobile

Table
-id
-available()

methods()
- find_available_table()
- reserve_table()
- unreserve_table()


Chef
- prepare_order()

Waiter
- server_order()

Reservation
- id
- start time
- end time
- table no


Order
- id
- items[]
- quantity


Items
- name
- price


OrderManagementSystem

Bill

Menu

Notification






