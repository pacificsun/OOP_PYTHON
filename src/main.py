class Item:
    # Construtor with quantity default to zero
    def __init__(self, name, price, quantity = 0):

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Laptop", 50, 3)
item2 = Item("Mobile", 10000, 20)

print(item2.name)

print(item1.calculate_total_price())

item1.has_numpad = False

print(item1.has_numpad)
