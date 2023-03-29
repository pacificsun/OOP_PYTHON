class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self, x, y):


        return x*y


item1 = Item("Laptop", 50, 3)
item2 = Item("Mobile", 10000, 20)


