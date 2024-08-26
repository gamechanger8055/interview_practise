from grokking.meeting_calendar.enums.meeting_status import Status


class UserMeetingDAO:
    def __init__(self):
        self.user_meetings={}

    def add_user_to_meeting(self,user_meeting):
        self.user_meetings[(user_meeting.meeting_id,user_meeting.user_id)]=user_meeting
        return user_meeting

    def update_user_meeting_status(self,meeting_id,user_id,status):
        user_meeting=self.user_meetings.get((meeting_id,user_id))
        if user_meeting:
            user_meeting.status=status
        return user_meeting

    def propose_time_change(self,meeting_id,user_id,proposed_time,decline_reason):
        user_meeting = self.user_meetings.get((meeting_id, user_id))
        if user_meeting:
            user_meeting.proposed_time_changes=proposed_time
            user_meeting.reason_for_declining=decline_reason
        return user_meeting

    def decline_meeting(self,meeting_id,user_id,reason_for_decline):
        user_meeting = self.user_meetings.get((meeting_id, user_id))
        if user_meeting:
            user_meeting.status = Status.DECLINED
            user_meeting.reason_for_declining=reason_for_decline
        return user_meeting