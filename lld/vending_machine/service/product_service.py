from lld.vending_machine.models.product import Product


class ProductService:
    def __init__(self,product_dao,inventory):
        self.product_dao=product_dao
        self.inventory=inventory

    def add_product(self,product_id, name, price, quantity):
        product=Product(product_id, name, price)
        self.product_dao.add_product(product)
        self.inventory.add_product(product, quantity)

    def get_product(self,product_id):
        return self.product_dao.get_product(product_id)

    def get_inventory(self,product_id):
        return self.inventory.get_product(product_id)