#Homework 3

grocery_items = ['Chicken', 'Steak', 'Fish', 'Apple']
grocery_item_prices = [10, 15, 25, 2]

print("Item: " + grocery_items[2] + " Price: " + grocery_item_prices[2])

prnt("Item: " + grocery_items[5] + " Price: " + grocery_item_prices[5])

grocery_items.append("Pineapple")
grocery_item_prices.append(4)

print(grocery_items)
print(grocery_item_prices)

del grocery_items[0]
del grocery_item_prices[0]

grocery_item_prices[1] = grocery_item_prices[2] * 2.0

print(grocery_items)
print(grocery_item_prices)