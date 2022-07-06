from menu_item import MenuItem

class Menu:
    #initialize with an array of menu items
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def show_menu(self):
        print("Coder Cafe Menu: ")
        for item in self.menu_items:
            item.show_item()

    def add_item(self,name,price):
        menu_item = MenuItem(name, price)
        self.menu_items.append(menu_item)

    def get_price(self, name):
        # return any(item for item in self.menu_items if item.name == name)
        for item in self.menu_items:
            if item.name == name:
                return item.price
        return False
    
    def delete_item(self,name):
        for item in self.menu_items:
            if item.name == name:
                self.menu_items.remove(item)
                return print(f"{name} removed from the menu")
        return print(f"{name} is not on the menu")

    def update_item(self,name):
        for item in self.menu_items:
            if item.name == name:
                price = float(input(f"What is the new price for {name}? "))
                item.price = price
                return print(f"{name} price updated")
        return print(f"{name} is not on the menu")

# item1 = MenuItem("Latte", 4.5)
# item2 = MenuItem("Capuccino", 4.5)
# item3 = MenuItem("Espresso", 3.5)

# items = []
# items.append(item1)
# items.append(item2)
# items.append(item3)

# coder_menu = Menu(items)

# coder_menu.show_menu()

# coder_menu.add_item("Muffin", 6.0)
# coder_menu.show_menu()
# print(coder_menu.find_item("Latte"))
# print(coder_menu.find_item("Coffee"))



