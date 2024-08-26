Google Meeting Calendar

- Users can create meeting
- Meeting can be one time or recurring.
- Meeting has list of participants, date, description.
- Participants can take actions on the event - Accept/decline, propose time change, reason
- User has a calendar which shows list of events/meetings - day/week/month/year

User
- id
- name
- email

Meeting
- id
- desciption
- date
- time
- recurrence_type one_time/recurring
- created_by_userid

Recurrence
- id
- meeting_id
- interval

User-Meeting
- meeting id
- user id
- status -accepted/declined/pending
- proposed_time_changes
- reason_for_declining