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

if "Chicken" in menu:
    first = list(menu)[0]       
    x = menu.get("Chicken")
    print(first + ": $" + str(x)) 
    
if "Pork" in menu:
    print("We do not have Pork")
else:
    print("We do not have Pork")

if "Mashed Potatoes" in menu:
    second = list(menu)[4]
    y = menu.get("Mashed Potatoes")
    print(second + ": $" + str(y)) 
print("--------------------")
print("Order Total: $" + str(x+y))

    