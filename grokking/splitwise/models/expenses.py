class Expense:
    def __init__(self, id, amount, paid_by, splits_strategy, description, date):
        self.id = id
        self.amount = amount
        self.paid_by = paid_by
        self.splits_strategy = splits_strategy
        self.description = description
        self.date = date