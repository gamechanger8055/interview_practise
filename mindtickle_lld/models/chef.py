from mindtickle_lld.models.person import Person
from mindtickle_lld.models.person_role import PersonRole


class Chef(Person):
    def __init__(self, name, mobile):
        super().__init__(name, mobile)
        self.role = PersonRole.CHEF

