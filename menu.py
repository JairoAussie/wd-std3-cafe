from menu_item import MenuItem

class Menu:
    # a list of menu items
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def print_menu(self):
        print("Welcome to Coder Cafe, this is our menu:")
        for item in self.menu_items:
            item.show_item()
    # adds a new item to the menu
    def add_item(self, name, price):
        #self.menu_items.append(MenuItem(name, price))
        new_item = MenuItem(name, price)
        self.menu_items.append(new_item)

    def delete_item(self, name):
        # iterate through the list looking for the item
        for item in self.menu_items:
            # check if the item's name of this iteration is equal to the name we receive.
            if item.name == name:
                # access to the list and remove the item
                self.menu_items.remove(item)
                return print(f"{name} was removed from the menu")
    
        return  print(f"{name} is not in the menu")   


# coffee1 = MenuItem("Latte", 4.5)
# coffee2 = MenuItem("Capuccino", 5.5)
# coffee3 = MenuItem("Espresso", 3.5)
# coffee4 = MenuItem("Tea", 4.0)

# menu = Menu([coffee1, coffee2, coffee3, coffee4])
# menu.print_menu()