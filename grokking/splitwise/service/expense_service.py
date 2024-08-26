from datetime import datetime
from grokking.splitwise.models.expenses import Expense

class ExpenseService:
    def __init__(self):
        self.expenses = {}

    def create_expense(self, id, amount, paid_by, splits, description, date=None):
        if id in self.expenses:
            raise ValueError("Expense with this ID already exists.")
        if date is None:
            date = datetime.now()
        expense = Expense(id, amount, paid_by, splits, description, date)
        self.expenses[id] = expense
        return expense

    def get_expense(self, id):
        if id not in self.expenses:
            raise ValueError("Expense not found.")
        return self.expenses[id]
