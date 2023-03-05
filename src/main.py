class Item:
    # Construtor with quantity default to zero
    def __init__(self, name: str, price: float, quantity = 0):

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Laotop", 50, 3)
item2 = Item("Mobile", 10000, 20)

print(item2.name)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

