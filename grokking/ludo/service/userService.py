from grokking.ludo.models.user import User

class UserService:

    def __init__(self):
        self.users={}

    def create_user(self,name,email="",username=None):
        if username in self.users:
            raise ValueError("user already exists")
        user=User(name,email,username)
        user.id_count+=1
        self.users[username]=user
        return user

    def get_user(self,username):
        return self.users[username]

    def get_all_users(self):
        return self.users

