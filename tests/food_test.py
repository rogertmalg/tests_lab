import unittest 

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("burger", 8)
        
    def test_food_has_name(self):
        self.assertEqual("burger", self.food.name)
        
    def test_food_has_price(self):
        self.assertEqual(8, self.food.price)

    