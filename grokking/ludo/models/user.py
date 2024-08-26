class User:
    def __init__(self,name,email,username):
        self.name=name
        self.email=email
        self.id_count=0
        self.username=username
        self.current_position=0

    def get_current_position(self):
        return self.current_position
