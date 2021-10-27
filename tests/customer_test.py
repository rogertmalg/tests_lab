import unittest 

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ted", 50)
        
    def test_customer_has_name(self):
        self.assertEqual("Ted", self.customer.name)
        
    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)