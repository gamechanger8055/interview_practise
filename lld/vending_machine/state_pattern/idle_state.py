from lld.vending_machine.state_pattern.state_interface import State


class IdleState(State):
    def __init__(self,vending_machine):
        self.vending_machine=vending_machine

    def select_product(self,product_id):
        product = self.vending_machine.product_service.get_product(product_id)
        if not product:
            print("Product not found")
        elif self.vending_machine.product_service.inventory.get_product(product_id)==0:
            print("Product out of stock")
        else:
            self.vending_machine.selected_product_id=product_id
            self.vending_machine.set_state(self.vending_machine.select_product_state)
            print(f"Product {product.name} selected")

    def insert_money(self, amount):
        print("Please select a product first")

    def dispense_product(self):
        print("Please select a product and insert money first")

