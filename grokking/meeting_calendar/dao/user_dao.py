from datetime import datetime


class UserDAO:
    def __init__(self):
        self.users={}

    def create(self,user):
        self.users[user.id]=user
        return user

    def get_by_id(self,user_id):
        return self.users.get(user_id)

    def delete(self,id):
        self.users.pop(id,None)

    def update_email(self,user_id,email):
        user=self.users[user_id]
        if user:
            user.email=email
            user.updated_at=datetime.now()
        return user
