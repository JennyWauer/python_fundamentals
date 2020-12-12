class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []
    
    def add_product(self, new_product):
        self.product_list.append(new_product)
    
    def sell_product(self, id):
        print(self.product_list[id])
        self.product_list.pop(id)

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

    def print_info(self):
        print(self)

store = Store("Ultra")