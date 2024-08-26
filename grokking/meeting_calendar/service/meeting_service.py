from grokking.meeting_calendar.models.meetings import Meeting


class MeetingService:
    def __init__(self,meeting_dao):
        self.meeting_dao=meeting_dao

    def create_meeting(self, id, description, date, recurrence_type, created_by_user_id,title):
        meeting = Meeting(title,description,id,date, created_by_user_id,recurrence_type)
        return self.meeting_dao.create(meeting)

    def get_meeting_by_id(self, id):
        return self.meeting_dao.get_by_id(id)

    def update_meeting(self, id, description, date, recurrence_type, created_by_user_id,title):
        meeting = Meeting(title,description,id,date, created_by_user_id,recurrence_type)
        return self.meeting_dao.update(meeting)

    def delete_meeting(self, id):
        return self.meeting_dao.delete(id)