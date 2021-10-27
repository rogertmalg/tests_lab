class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def buy_drink(self, pub, drink):
        self.wallet -= drink.price
        pub.sell_drink(drink)

    
        
     