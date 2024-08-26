from datetime import datetime


class Meeting:
    def __init__(self,title,description,id,date, created_by,recurrence_type):
        self.title=title
        self.desc=description
        self.id=id
        self.date=date
        self.created_by=created_by
        self.recurrence_type=recurrence_type
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
