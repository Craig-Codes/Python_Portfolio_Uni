# Product break even data

production_cost = 20.00
sales_price = 40.00
fixed_costs = 50000.00
breakeven_amount = fixed_costs / (sales_price - production_cost)

print("Cost to produce each item: £{}".format(production_cost))
print("Sales price for each item: £{}".format(sales_price))
print("Profit per item: £{}".format(sales_price - production_cost))
print("Breakeven: {} items".format(int(breakeven_amount)))