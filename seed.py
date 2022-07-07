from menu_item import MenuItem
from menu import Menu
# seed the Menu put of the main file
def seed():
    coffee1 = MenuItem("Latte", 4.5)
    coffee2 = MenuItem("Capuccino", 5.5)
    coffee3 = MenuItem("Espresso", 3.5)
    coffee4 = MenuItem("Tea", 4.0)
    menu = Menu([coffee1, coffee2, coffee3, coffee4])
    return menu