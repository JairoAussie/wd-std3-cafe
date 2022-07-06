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

    def find_item(self, name):
        # return any(item for item in self.menu_items if item.name == name)
        for item in self.menu_items:
            if item.name == name:
                return item
        return False
    
    def delete_item(self,item):
        self.menu_items.remove(item)

item1 = MenuItem("Latte", 4.5)
item2 = MenuItem("Capuccino", 4.5)
item3 = MenuItem("Espresso", 3.5)

items = []
items.append(item1)
items.append(item2)
items.append(item3)

coder_menu = Menu(items)

coder_menu.show_menu()

coder_menu.add_item("Muffin", 6.0)
coder_menu.show_menu()
print(coder_menu.find_item("Latte"))
print(coder_menu.find_item("Coffee"))




#     #find item, it receives a name, it returns the index if the item was found, -1 if not found
#     def find_item(name)
#         #to return the index
#         @menu_items.each_with_index do |item, index|
#             if item.name == name
#                 return index
#             end
#         end
#         return -1
#         #to return the object
#         # item = @menu_items.find{|item| item.name=name}
#     end

#     #delete item, receives the index, and deletes that item
#     def delete_item(index)
#         #receiving an object ->  @menu_items.delete(item)
#         @menu_items.delete_at(index)
#     end
#     #edit item, it receives the index, and edits that item 
#     def edit_item(index, price)
#         @menu_items[index].price = price
#     end

#     #returns the price of a given menu_item
#     def get_price(name)
#         #find the object in the array by name
#         menu_item = @menu_items.find{|item| item.name == name}
#         return menu_item.price
#     end
# end