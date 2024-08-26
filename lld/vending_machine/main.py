# Define the services
from lld.vending_machine.dao.product_dao import ProductDAO
from lld.vending_machine.models.inventory import Inventory
from lld.vending_machine.service.payment_service import PaymentService
from lld.vending_machine.service.product_service import ProductService
from lld.vending_machine.vending_machine import VendingMachine

product_dao = ProductDAO.get_instance()
inventory = Inventory()
product_service = ProductService(product_dao, inventory)
payment_service = PaymentService()

# Add some products
product_service.add_product(1, "Coke", 2.50, 10)
product_service.add_product(2, "Pepsi", 1.25, 5)

# Create the vending machine
vending_machine = VendingMachine(product_service, payment_service)

# Use the vending machine
vending_machine.select_product(1)
vending_machine.insert_money(1.00)
vending_machine.insert_money(0.50)
vending_machine.dispense_product()

# Output:
# Product Coke selected
# Please insert more money
# Sufficient money inserted
# Dispensing Coke
