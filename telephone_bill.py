# Prompt user for number of minutes
minutes = int(input("Enter number of minutes used to the nearest whole number: "))
print("Number of minutes used: {}".format(minutes))

# Calculate and print the call charge at 15p per minute
call_charge = minutes * 0.15
# Ensure only 2 decimal places are shown
print("Basic call charge: £{:.2f}".format(call_charge))

# Calculate and output the VAT due at 20%
vat = call_charge * 0.2
print("VAT due: £{:.2f}".format(vat))

# Calculate and output the bill total, by adding vat to call_charge
total = call_charge + vat
print("Total bill: £{:.2f}".format(total))
