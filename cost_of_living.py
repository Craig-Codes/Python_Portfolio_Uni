from tabulate import tabulate
# Tabulate package used to output user data in a neat table structure

# Get the user inputs and store them in variables
rent = float(input("Rent costs: "))
gas = float(input("Gas costs: "))
electricity = float(input("Electricity costs: "))
water = float(input("Water costs: "))
council_tax = float(input("Council Tax costs: "))

# Variable to store the user input total sum
total = rent + gas + electricity + water + council_tax

# Create a table for tabulate to use to output the data
table = [["Rent:", "£", rent],
         ["Gas:", "£", gas],
         ["Electricity:", "£", electricity],
         ["Water:", "£", water],
         ["Council Tax:", "£", council_tax]]

print("Your monthly expenses are:")
# Print a plain table, ensuring 2 decimal places are always shown
print(tabulate(table, tablefmt="plain", floatfmt=".2f"))
# Print the total ensuring 2 decimal places are always shown
print("=======================")
print("Total:        £ ", f'{total:.2f}')
print("=======================")



