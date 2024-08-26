class Inventory:
    def __init__(self):
        self.stocks={}

    def add_product(self,product,quantity):
        if product.product_id in self.stocks:
            self.stocks[product.product_id]+=quantity
        else:
            self.stocks[product.product_id] = quantity

    def remove_product(self,product_id, quantity):
        if product_id in self.stocks and self.stocks[product_id]>=quantity:
            self.stocks[product_id] -= quantity
            return True
        return False

    def get_product(self,product_id):
        return self.stocks.get(product_id,0)
