class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []
    
    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self
    
    def sell_product(self, id):
        print(self.product_list[id])
        self.product_list.pop(id)
        return self

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

# Test cases
ultra = Store("Ultra")

shampoo = Product("shampoo", 5.55, "hair care")
conditioner = Product("conditioner", 4.99, "hair care")
nail_polish = Product("nail polish", 3.69, "nail care")

ultra.add_product(shampoo).add_product(conditioner).add_product(nail_polish).sell_product(1)

shampoo.update_price(0.15, True).print_info()
nail_polish.update_price(0.08, False).print_info()