from grokking.ludo.models.jump import Jump
from grokking.ludo.service.userService import UserService
from grokking.ludo.models.user import User


class SnakeAndLadderService:
    def __init__(self):
        self.jumps={}
        self.user_service=UserService()

    def add_jumps(self,id,start,end):
        if id not in self.jumps:
            jump=Jump(id,start,end)
            self.jumps[id]=jump

    def get_jumps(self,jump_id):
        return self.jumps[jump_id]

    def get_all_jumps(self):
        return self.jumps

    def new_position(self,user,dice_count):
        for jump_id in self.jumps:
            if user.current_position+dice_count==self.jumps[jump_id].start:
                user.current_position=self.jumps[jump_id].end
                return user.current_position
        user.current_position=user.current_position+dice_count
        return user.current_position








