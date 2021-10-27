class Pub:
    def __init__(self, name, till):
       self.name = name
       self.till = till
    #    self.drinks = {}
       self.stock = {}

    def sell_drink(self, drink):
        self.till += drink.price

    def can_drink(self, customer):
        if customer.age >= 18 and customer.drunkness <= 5:
            return True
         
        return False

    def add_drink(self, drink): 
        if drink in self.stock:
            self.stock[drink] += 1
        else:
            self.stock[drink] = 1    

    def stock_level(self, drink): 
        if drink in self.stock:
            return self.stock[drink]
        else:
            return 0

    def stock_value(self):
        total = 0
        for drink in self.stock:
            total += (drink.price * self.stock[drink]) 
        
        return total
