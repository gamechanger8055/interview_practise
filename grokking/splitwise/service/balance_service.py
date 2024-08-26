class BalanceService:
    def __init__(self):
        self.balances = {}

    def calculate_balance(self, group):
        balances = {member: 0.00 for member in group.members}
        for expense in group.expenses:
            for split in expense.splits:
                balances[split.user] += split.amount
            balances[expense.paid_by] -= expense.amount
        return balances

    def update_balance(self, user, group, amount):
        key = (user.id, group.id)
        if key not in self.balances:
            self.balances[key] = 0.0
        self.balances[key] += amount

