class Order:
    # initialise it with order_items, which is an empty dictionary => {product: quantity}
    # order_items = {"Latte" : 4, "Espresso": 1, "Tea": 2}
    def __init__(self):
        self.order_items = {}

    # Add an item to the order
    def add_item_to_order(self, name, quantity):
        # ask if the name is already in the dictionary
        if name in self.order_items:
            # if the name already is in the dictionary, let's increment the quantity
            self.order_items[name] += quantity
        else: 
            # if the name is not in the dictionary, let's assign the quantity
            self.order_items[name] = quantity

    def calculate_total_bill(self):
        total = 0
        for name, quantity in self.order_items.items():
            price = 5 # how can I get it?
            total += price * quantity
        return f"Total bill: ${total}"
# order = Order()
# order.add_item_to_order("Latte", 2)
# order.add_item_to_order("Espresso", 1)
# order.add_item_to_order("Latte", 1)
# print(order.order_items)