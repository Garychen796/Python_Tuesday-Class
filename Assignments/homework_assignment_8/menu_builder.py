# Guanyu Chen
# 0953074
# 11/03/2019
# MSITM 6341

print("-----------------------------------------")
print("Please enter the menu items for the Restaurant")
print("-----------------------------------------")

menu_items = {}

should_ask_for_item = True

while should_ask_for_item:

    item = input("Item Name: ")
    cost = input("Item Cost: ")

    if item in menu_items:
        print("WARNING: Item exists")
        
    menu_items[item] = cost
    

    containue_or_not = input("Continue(Y/N)? ")

    if containue_or_not == "N":
        should_ask_for_item = False
print("-----------------------------------------")
print("Restaurant Menu")
print("-----------------------------------------")

for item, cost in menu_items.items():
    print("Item Name: " + item + "Cost: " + cost)

print("-----------------------------------------")