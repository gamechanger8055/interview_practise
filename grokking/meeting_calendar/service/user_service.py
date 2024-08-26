from grokking.meeting_calendar.models.user import User

class UserService:
    def __init__(self,user_dao):
        self.user_dao=user_dao

    def create_user(self,id,name,email):
        user=User(id,name,email)
        return self.user_dao.create(user)

    def get_user_by_id(self, id):
        return self.user_dao.get_by_id(id)

    def update_user_email(self, id, email):
        return self.user_dao.update_email(id, email)

    def delete_user(self, id):
        return self.user_dao.delete(id)
