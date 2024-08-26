import unittest
from mindtickle_lld.service.order_management import OrderManagementSystem
from mindtickle_lld.service.restaurant_management import RestaurantManagement
from mindtickle_lld.models.item import Item

class RmsTesting(unittest.TestCase):
    def setUp(self):
        self.restaurant_mgmt=RestaurantManagement()
        self.order_mgmt=OrderManagementSystem()

    def test_create_order(self):
        self.order_mgmt.create_order(1,Item("roti",20),2)
        self.order_mgmt.create_order(1, Item("paneer", 200), 2)
        print(self.order_mgmt.orders)

    def test_reserve_table(self):
        self.restaurant_mgmt.reserve_table()
        print(self.restaurant_mgmt.tables)

    def test_generate_bill(self):
        self.order_mgmt.create_order(1, Item("roti", 20), 2)
        self.order_mgmt.create_order(1, Item("paneer", 200), 2)
        print(self.order_mgmt.orders)
        print(self.order_mgmt.generate_bill(1))

# if __name__=="main":
#     unittest.main()