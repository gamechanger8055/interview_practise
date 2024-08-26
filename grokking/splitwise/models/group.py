class Group:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.members=[]
        self.expenses=[]

    def add_member(self,user):
        self.members.append(user)

    def add_expense(self,expense):
        self.expenses.append(expense)
    