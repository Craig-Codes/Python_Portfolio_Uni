# Program prompts for number and value of shopping list items, outputting the total at the end

peaches_quantity = int(input("How many peaches did you buy?"))
peaches_price = float(input("How much did the peaches cost?"))
beans_quantity = int(input("How many tins of beans did you buy?"))
beans_price = float(input("How much did the beans cost?"))
chicken_quantity = int(input("How many packets of chicken pieces did you buy?"))
chicken_price = float(input("How much did the chicken cost?"))
socks_quantity = int(input("How many pairs of socks did you buy?"))
socks_price = float(input("How much did the socks cost?"))
water_quantity = int(input("How many bottles of water did you buy?"))
water_price = float(input("How much did the water cost?"))

item_number = peaches_quantity + beans_quantity + chicken_quantity + socks_quantity + water_quantity
item_price_total = peaches_price + beans_price + chicken_price + socks_price + water_price

print("Peaches:")
print("- How many? ", peaches_quantity)
print("- Price? ", peaches_price)
print("Beans:")
print("- How many? ", beans_quantity)
print("- Price? ", beans_price)
print("Chicken pieces:")
print("- How many? ", chicken_quantity)
print("- Price? ", chicken_price)
print("Socks:")
print("- How many? ", socks_quantity)
print("- Price? ", socks_price)
print("Bottle of water:")
print("- How many? ", water_quantity)
print("- Price? ", water_price)

print("Total number of items purchased: {}".format(item_number))
print("Your weekly shopping cost: {}".format(item_price_total))
