from grokking.meeting_calendar.models.user_meeting import UserMeeting


class UserMeetingService:
    def __init__(self, user_meeting_dao):
        self.user_meeting_dao = user_meeting_dao

    def add_user_to_meeting(self, meeting_id, user_id, status):
        user_meeting = UserMeeting(meeting_id, user_id, status)
        return self.user_meeting_dao.add_user_to_meeting(user_meeting)

    def update_user_meeting_status(self, meeting_id, user_id, status):
        return self.user_meeting_dao.update_user_meeting_status(meeting_id, user_id, status)

    def propose_time_change(self, meeting_id, user_id, proposed_time_changes, reason_for_declining):
        return self.user_meeting_dao.propose_time_change(meeting_id, user_id, proposed_time_changes, reason_for_declining)

    def decline_meeting(self, meeting_id, user_id, reason_for_declining):
        return self.user_meeting_dao.decline_meeting(meeting_id, user_id, reason_for_declining)