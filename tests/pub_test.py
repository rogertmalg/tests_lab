import unittest 

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Spoons", 500)
    
    def test_pub_has_name(self):
        self.assertEqual("Spoons", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(500, self.pub.till)
    
    def test_sell_drink(self):
        drink = Drink("beer", 5)
        self.pub.sell_drink(drink)
        self.assertEqual(505, self.pub.till)

    def test_customer_can_drink_true(self):
        customer = Customer("ted", 50, 18)
        self.assertEqual(True, self.pub.can_drink(customer))

    def test_customer_can_drink_false(self):
        customer2 = Customer("Angela", 50, 17)
        self.assertEqual(False, self.pub.can_drink(customer2))