from lld.vending_machine.state_pattern.idle_state import IdleState
from lld.vending_machine.state_pattern.make_payment_state import MakePaymentState
from lld.vending_machine.state_pattern.select_product_state import SelectProductState


class VendingMachine:
    def __init__(self,product_service,payment_service):
        self.product_service=product_service
        self.payment_service=payment_service
        self.selected_product_id=None
        self.idle_state=IdleState(self)
        self.make_payment_state=MakePaymentState(self)
        self.select_product_state=SelectProductState(self)
        self.current_state=self.idle_state

    def set_state(self,state):
        self.current_state=state

    def select_product(self,product_id):
        self.current_state.select_product(product_id)

    def insert_money(self,amount):
        self.current_state.insert_money(amount)

    def dispense_product(self):
        self.current_state.dispense_product()




