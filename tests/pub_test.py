import unittest 

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

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
        drink = Drink("beer", 5)
        customer.buy_drink(self.pub, drink)
        customer.buy_drink(self.pub, drink)
        customer.buy_drink(self.pub, drink)
        self.assertEqual(True, self.pub.can_drink(customer))

    def test_customer_can_drink_false(self):
        customer2 = Customer("Angela", 50, 17)
        drink = Drink("beer", 5)
        customer2.buy_drink(self.pub, drink)
        customer2.buy_drink(self.pub, drink)
        customer2.buy_drink(self.pub, drink)
        customer2.buy_drink(self.pub, drink)
        customer2.buy_drink(self.pub, drink)
        customer2.buy_drink(self.pub, drink)
        self.assertEqual(False, self.pub.can_drink(customer2))

    def test_add_drink_to_stock(self):
        drink = Drink("beer", 5)
        self.pub.add_drink(drink) 
        self.assertEqual(1, len(self.pub.stock))

    def test_stock_level_is_0(self):
        drink = Drink("beer", 5)
        self.assertEqual(0, self.pub.stock_level(drink))

    def test_stock_level_is_1(self):
        drink = Drink("beer", 5)
        self.pub.add_drink(drink)
        self.assertEqual(1, self.pub.stock_level(drink))

    def test_stock_value_15(self):
        drink = Drink("beer", 5)
        self.pub.add_drink(drink)
        self.pub.add_drink(drink)
        self.pub.add_drink(drink)
        self.assertEqual(15, self.pub.stock_value())