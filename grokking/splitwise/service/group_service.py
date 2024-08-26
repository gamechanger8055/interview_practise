from grokking.splitwise.models.group import Group

class GroupService:
    def __init__(self):
        self.groups = {}

    def create_group(self, id, name):
        if id in self.groups:
            raise ValueError("Group with this ID already exists.")
        group = Group(id, name)
        self.groups[id] = group
        return group

    def get_group(self, id):
        if id not in self.groups:
            raise ValueError("Group not found.")
        return self.groups[id]

    def add_member_to_group(self, group_id, user):
        group = self.get_group(group_id)
        group.add_member(user)

    def remove_member_from_group(self, group_id, user):
        group = self.get_group(group_id)
        group.remove_member(user)
