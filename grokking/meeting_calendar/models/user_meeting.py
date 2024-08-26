
class UserMeeting:
    def __init__(self, meeting_id, user_id, status, proposed_time_changes=None, reason_for_declining=None):
        self.meeting_id = meeting_id
        self.user_id = user_id
        self.status = status
        self.proposed_time_changes = proposed_time_changes
        self.reason_for_declining = reason_for_declining