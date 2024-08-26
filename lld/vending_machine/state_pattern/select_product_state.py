from lld.vending_machine.state_pattern.state_interface import State


class SelectProductState(State):
    def __init__(self,vending_machine):
        self.vending_machine=vending_machine

    def select_product(self,product_id):
        print("Product already selected. Please insert money")

    def insert_money(self, amount):
        self.vending_machine.payment_service.process_payment(amount)
        product = self.vending_machine.product_service.get_product(self.vending_machine.selected_product_id)
        if self.vending_machine.payment_service.get_balance()>=product.price:
            self.vending_machine.set_state(self.vending_machine.make_payment_state)
            print("Sufficient money inserted")
        else:
            print("Please insert more money")


    def dispense_product(self):
        print("Please insert money first")

