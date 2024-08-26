from grokking.splitwise.service.group_service import GroupService
from grokking.splitwise.service.balance_service import BalanceService
from grokking.splitwise.service.expense_service import ExpenseService
from grokking.splitwise.service.user_service import UserService
from grokking.splitwise.service.split_strategy import EqualStrategy
from grokking.splitwise.service.split_strategy import PercentageSplit
# Create instances of the services
user_service = UserService()
group_service = GroupService()
expense_service = ExpenseService()
balance_service = BalanceService()

# Create users
user1 = user_service.create_user(1, "Alice", "alice@example.com", "1234567890")
user2 = user_service.create_user(2, "Bob", "bob@example.com", "0987654321")

# Create a group and add users to the group
group = group_service.create_group(1, "Trip to Spain")
group_service.add_member_to_group(group.id, user1)
group_service.add_member_to_group(group.id, user2)

# Create an equal split expense and add it to the group
equal_split_strategy = EqualStrategy()
expense1 = expense_service.create_expense(1, 100, user1, equal_split_strategy, "Dinner at restaurant")
group.add_expense(expense1)

# Create a percentage split expense and add it to the group
percentage_split_strategy = PercentageSplit([70, 30])
expense2 = expense_service.create_expense(2, 200, user2, percentage_split_strategy, "Hotel stay")
group.add_expense(expense2)

print(group)
# Calculate the balances
balances = balance_service.calculate_balance(group)
for user, balance in balances.items():
    print(f"{user.name} owes {balance}")
