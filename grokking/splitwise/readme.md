Requirements
- User/Group registration and management
- Add expenses withing groups
- Splitting expenses within group
- View balance of each individual
- Settling balances

DB schema Design

User
- id
- name
- email
- phone
- group_id

Group
- id
- name
- members_count

Expenses
- id
- group_id
- amount
- paid_by_user id(fk to user)
- datetime

Balance
- user id
- amount
- group id

Split
- id
- balance id
- user id
- amount

Settlement
- id
- from user id
- to user id
- amount
- group id
- amount
- datetime


API design

- /create_expense()
- /settle()
- /get_balanece()

