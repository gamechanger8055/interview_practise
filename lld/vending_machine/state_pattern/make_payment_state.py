from lld.vending_machine.state_pattern.state_interface import State


class MakePaymentState(State):
    def __init__(self,vending_machine):
        self.vending_machine=vending_machine

    def select_product(self,product_id):
        print("Money already inserted. Please wait for dispensing")

    def insert_money(self, amount):
        print("Money already inserted. Please wait for dispensing")


    def dispense_product(self):
        product = self.vending_machine.product_service.get_product(self.vending_machine.selected_product_id)
        if not product:
            print("Product not found")
            self.vending_machine.set_state(self.vending_machine.idle_state)
        elif self.vending_machine.product_service.inventory.get_product(self.vending_machine.selected_product_id):
            print("Product out of stock")
            self.vending_machine.set_state(self.vending_machine.idle_state)
            self.vending_machine.payment_service.refund_payment()
        else:
            self.vending_machine.product_service.inventory.remove_product(self.vending_machine.selected_product_id, 1)
            print(f"Dispensing {product.name}")
            self.vending_machine.payment_service.process_payment(-product.price)
            self.vending_machine.set_state(self.vending_machine.idle_state)



