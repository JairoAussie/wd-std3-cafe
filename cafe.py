from os import system
from seed import seed
from order import Order

menu = seed()

def print_options():
    print("1. Show menu")
    print("2. Add product to the menu")
    print("3. Edit price of a product from the menu")
    print("4. Delete a product from the menu")
    print("5. Take an order")
    print("6. Exit")
    opt = input("Select your option (1-6): ")
    return opt


def add_product():

    name = input("What's the name of the new product? ")
    price = float(input (f"What's the price of {name}? "))
    menu.add_item(name, price)
    print(f"{name} being added to the menu...")
    #add menu item to the menu


def delete_product():
    #show the list of products, just names
    for item in menu.menu_items:
        print(item.name)
    #ask about the product we want to delete
    name = input("What is the product you want to delete? ")
    menu.delete_item(name)
    #make sure it is in the menu

    #delete it

def edit_product():
    menu.print_menu()
    #ask about the product we want to delete
    name = input("What is the product you want to edit? ")
    #make sure it is in the menu
    menu.update_price(name)
    #ask for the new price

def take_order():
    print("start a new order...")
    #create a new order
    new_order = Order()
    cont = "y"
    #start adding items to the order, ask if there are more items each time after
    while cont == "y":
        name = input("What can I get for you? ")
        quantity = int(input("How many of them? "))
        new_order.add_item_to_order(name, quantity)
        cont = input("Anything else? (y/n) ")
    #when all the items are added show the total price of the order.
    print(new_order.order_items)
    print(new_order.calculate_total_bill())

option = ""

while option != "6":
    system('clear')
    option = print_options()
    system('clear')
    if option == "1":
        menu.print_menu()
    elif option == "2":
        add_product()
    elif option == "3":
        edit_product()
    elif option == "4":
        delete_product()
    elif option == "5":
        take_order()
    elif option == "6":
        continue
    else:
        print("Invalid option")
        
    input("press Enter to continue...")
    system('clear')

print("Goodbye!") 
