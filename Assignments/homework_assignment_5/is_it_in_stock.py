# Guanyu Chen
# 0953074
# 09/29/2019
# MSITM 6341

menu_items_in_stock = ["Tacos", "Chips", "Salsa", "Quesadilla"]

customer_order = ["Tacos", "Guacamole", "Burrito", "Chips", "Salsa"]

for item in menu_items_in_stock:
    item = item.lower()

for order in customer_order:
    order = order.lower()


for order in customer_order:
    if order in menu_items_in_stock:
        print("We have " + order.capitalize() + " in stock.")
    else:
        print("We do not have " + order.capitalize() + " in stock.")