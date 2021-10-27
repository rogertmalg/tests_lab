import unittest 

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ted", 50, 18)
        
    def test_customer_has_name(self):
        self.assertEqual("Ted", self.customer.name)
        
    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(18, self.customer.age)

    def test_buy_drink(self):
        pub = Pub("Spoons", 500)
        drink = Drink("beer", 5)
        self.customer.buy_drink(pub, drink)
        self.assertEqual(45, self.customer.wallet)
        self.assertEqual(505, pub.till)
    
    def test_customer_drunkness(self):
        pub = Pub("Spoons", 500)
        drink = Drink("beer", 5)
        self.customer.buy_drink(pub, drink)
        self.assertEqual(1, self.customer.drunkness)

    
           

