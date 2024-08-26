from collections import defaultdict
from mindtickle_lld.models.order import Order
class OrderManagementSystem:
    def __init__(self):
        self.orders=defaultdict(list)

    def create_order(self,id,item,quantity):
        self.orders[id].append(Order(id,item,quantity))


    def generate_bill(self,id):
        total_cost=0
        for order in self.orders[id]:
            total_cost+=order.items.price*order.quantity
        return total_cost



