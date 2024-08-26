from abc import ABC,abstractmethod
from grokking.splitwise.models.split import Split

class SplitStrategy(ABC):
    @abstractmethod
    def calculate_splits(self,amount,members):
        pass

class EqualStrategy(SplitStrategy):
    def calculate_splits(self,amount,members):
        split_amount=amount/members
        return [Split(member,split_amount) for member in members]

class PercentageSplit(SplitStrategy):
    def __init__(self, percentages):
        self.percentages = percentages

    def calculate_splits(self, amount, members):
        if len(self.percentages) != len(members):
            raise ValueError("Number of percentages must match number of members.")
        return [Split(member, amount * percentage / 100) for member, percentage in zip(members, self.percentages)]
