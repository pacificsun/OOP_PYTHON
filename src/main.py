class Item:
    pay_rate = 0.8 # The pay rate after 20% discount, This is class attribute
    # Construtor with quantity default to zero
    def __init__(self, name: str, price: float, quantity = 0):
        print(f"An instance creted: {name}")

        # Run validations to the received arguments

        assert price >= 0, f"Price {price} is not grater than zero"
        assert quantity >=0, f"Quantity{quantity} is not greater than zero!"

        # Assign to self object
        # naya object banda kheri tini haru value deko
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        


item1 = Item("Laotop", 50, 3)
item2 = Item("Mobile", 10000, 20)

# print(item2.name)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.__dict__) # All the attributes for Class level
# print(item1.__dict__) # All the attributess for instance level

