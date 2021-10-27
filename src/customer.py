class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age 
    
    def buy_drink(self, pub, drink):
        self.wallet -= drink.price
        pub.sell_drink(drink)

    
        
     