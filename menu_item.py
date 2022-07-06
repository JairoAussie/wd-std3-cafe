class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_item(self):
        print(f"{self.name}: ${self.price}")


# coffe1 = MenuItem("Latte", 4.5)

# print(coffe1.name)
# print(coffe1.price)
# coffe1.show_item()