class MenuItem:
    #name, price,
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_item(self):
        print(f"{self.name}: ${self.price}")

# coffee1 = MenuItem("Latte", 4.5)
# coffee1.show_item()

