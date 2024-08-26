class Expense:
    def __init__(self,expense_id,description,amount,paid_by, split_between,split_strategy=None):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.split_strategy=split_strategy
        self.split_between = split_between
        self.splits=self.calculate_splits()

    def calculate_splits(self):
        individual_amount=self.amount/len(self.split_between)
        return {user_id:individual_amount for user_id in self.split_between}




