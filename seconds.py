from tabulate import tabulate
# Tabulate package used to output user data in a neat table structure

# Get the user input of seconds
time = int(input("Please enter a positive whole number of seconds: "))

# to get hours we use the floor division operator to always get the rounded down integer
hours = time // 3600
# to get minutes we need to firstly get the remainder from the hours figure using modulus operator
hours_remainder = time % 3600
# we now divide the remainder by 60 to get the minutes, again rounding down
minutes = hours_remainder // 60
# to get the seconds we then need to get the remainder of the minutes value
minutes_remainder = hours_remainder % 60
# seconds are anything left over
seconds = minutes_remainder

# Create a tabulate table
table = [["Input", "Hours", "Minutes", "Seconds"],
         [time, hours, minutes, seconds]]

# Print the table, in plain format with the values aligned to the right
print(tabulate(table, tablefmt="plain", stralign="right"))
