# Guanyu Chen
# 0953074
# 09/15/2019
# MSITM 6341

grocery_store_items = ['Apple', 'Milk','Beef', 'Banana', 'Juice']
grocery_price = ['2', '3', '4', '1', '5']

print("Item: " + grocery_store_items[2] + ", Price: " + "$" + grocery_price[2])

print("Item: " + grocery_store_items[4] + ", Price: " + "$" + grocery_price[4])

grocery_store_items.append('Pineapple')
grocery_price.append('6')

print(grocery_store_items)
print(grocery_price)

del grocery_store_items[0]
del grocery_price[0]

grocery_price[1] = str(2*int(grocery_price[1]))

print(grocery_store_items)
print(grocery_price)
