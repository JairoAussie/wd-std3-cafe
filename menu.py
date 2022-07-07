from menu_item import MenuItem

class Menu:
    # a list of menu items
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def print_menu(self):
        print("Welcome to Coder Cafe, this is our menu:")
        for item in self.menu_items:
            item.show_item()

    
# coffee1 = MenuItem("Latte", 4.5)
# coffee2 = MenuItem("Capuccino", 5.5)
# coffee3 = MenuItem("Espresso", 3.5)
# coffee4 = MenuItem("Tea", 4.0)

# menu = Menu([coffee1, coffee2, coffee3, coffee4])
# menu.print_menu()