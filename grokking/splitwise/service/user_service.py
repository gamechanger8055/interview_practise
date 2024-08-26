from grokking.splitwise.models.user import User

class UserService:
    def __init__(self):
        self.users={}

    def create_user(self, id, name, email, phone):
        if id in self.users:
            raise ValueError("users with this ID already exists")
        user=User(id,name,email,phone)
        self.users[id]=user
        return user

    def get_user(self,id):
        if id not in self.users:
            raise ValueError(f'user does not exist with this id {id}')
        return self.users[id]

    def update_user(selfid, name, email, phone):
        pass
