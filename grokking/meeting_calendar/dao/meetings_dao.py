class MeetingDAO:
    def __init__(self):
        self.meetings={}

    def create(self,meeting):
        self.meetings[meeting.id]=meeting
        return meeting

    def get_by_id(self,meeting_id):
        return self.meetings.get(meeting_id)

    def delete(self,id):
        self.meetings.pop(id,None)

    def update_email(self,meeting):
        if meeting.id in self.meetings:
            self.meetings[meeting.id]=meeting
        return meeting
