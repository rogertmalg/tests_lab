import unittest 

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("beer", 5)
        
    def test_drink_has_name(self):
        self.assertEqual("beer", self.drink.name)
        
    def test_drink_has_price(self):
        self.assertEqual(5, self.drink.price)  
    
      
    