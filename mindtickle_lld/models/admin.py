from mindtickle_lld.models.person import Person
from mindtickle_lld.models.person_role import PersonRole

class Admin(Person):
    def __init__(self,name,mobile):
        super().__init__(name,mobile)
        self.role=PersonRole.ADMIN

    def reserve_table(self):


