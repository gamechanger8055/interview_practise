class PaymentService:
    def __init__(self):
        self.amount_received=0

    def process_payment(self, amount):
        self.amount_received += amount

    def refund_payment(self):
        refund_amount = self.amount_received
        self.amount_received = 0
        return refund_amount

    def get_balance(self):
        return self.amount_received