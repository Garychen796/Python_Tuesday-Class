# Guanyu Chen
# 0953074
# 10/29/2019
# MSITM 6341

menu = {
		"Chicken" : 10.0,
		"Beef" : 14.0,
		"Fries" : 2.0,
		"Coke" : 1.0,
		"Mashed Potatoes" : 5.0
	}

customer_order = []
menu_name = ''
total = 0

while menu_name != 'N':
    menu_name  = input('Enter an item: ')
    if menu_name  != 'N':
        customer_order.append(menu_name)

print('')
   
    
for item in customer_order:
    if item in menu:
        item_price = menu.get(item)
        print("{}: ${:.1f}".format(item,item_price))
        total += item_price
    else:
        print('We do not have ' + item)

print("---------------------")
print("Order Total: ${:.1f}".format(total))
