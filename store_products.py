class Store:
    def __init__(self, name, product_list):
        self.name = name
        self.product_list = []

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category