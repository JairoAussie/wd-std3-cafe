class Order:
    #initialize it with order_items, and empty hash. {product => quantity}
    def __init__(self):
        self.order_items = {}

    def add_order_line(self, name, quantity): #Espresso , 1
        if name in self.order_items:
            self.order_items[name] += quantity 
        else:
            self.order_items[name] = quantity

    #it returns the total price of the order, we need the menu
    def total_order(self, menu):
        total = 0
        for name, quantity in self.order_items.items():
            price = menu.get_price(name)
            total += price * quantity
        return total
