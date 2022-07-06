from menu import Menu
from menu_item import MenuItem

def seed():
    menu = Menu([MenuItem("Latte", 4.5),MenuItem("Espresso", 3.5),MenuItem("Capuccino", 5.0),MenuItem("Tea", 4.0)])
    return menu