class Store:
    def __init__(self, name, product_list):
        self.name = name
        self.product_list = []

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            increase = self.price * percent_change
            self.price += increase
            return self
        else:
            decrease = self.price * percent_change
            self.price -= decrease
            return self