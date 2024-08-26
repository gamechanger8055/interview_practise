from datetime import datetime


class User:
    def __init__(self,id,name,email):
        self.id=id
        self.email=email
        self.name=name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
