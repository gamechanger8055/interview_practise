class ProductDAO:
    _instance=None

    @staticmethod
    def get_instance(): #singleton method
        if not ProductDAO._instance:
            ProductDAO._instance=ProductDAO()
        return ProductDAO._instance

    def __init__(self):
        if ProductDAO._instance:
            raise Exception("This class is a singleton!")
        self.products={}

    def add_product(self,product):
        self.products[product.product_id]=product

    def get_product(self, product_id):
        return self.products.get(product_id)