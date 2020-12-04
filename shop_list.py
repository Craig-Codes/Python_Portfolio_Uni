shopping_list = []  # list to store all of the items and price data
sorted_list = []  # list to store the sorted items based on prices

# Get the user inputs to build the list
for i in range(5):  # loop through 5 times, requesting 5 inputs
    name_input = str(input("Enter the items name: "))
    while True:  # make sure we get a valid number input
        try:
            price = float(input("Enter the items price (£): "))
            price = format(price, '.2f')  # format price to two decimal places
            price = float(price)  # turn the rounded number back into a float so it can be used as a number again
            break  # valid price so break - could add more checks here to limit to two decimal places etc
        except ValueError:
            print("Enter a valid number input for the items price")
            continue  # go back to start of loop to get a valid price

    shopping_list.append([name_input, price])  # append a new list to the list featuring the items name and price

for item in shopping_list:  # loop through the list of lists
    sorted_list.append(item)  # add item to the end of the sorted list - ensures sorted_list always has an entry
    for i in range(len(sorted_list)):  # loop over each item in the sorted list
        # if the item price is greater than the current item price, add the item to the list before that current entry
        if item[1] > sorted_list[i][1]:
            sorted_list.insert(i, item)
            sorted_list.pop()  # found the item and inserted it, so can pop off the end to avoid double entries
            break

print("\nYour list sorted by numerical value is:")
for item in sorted_list:
    print("{} £{:.2f}".format(item[0], item[1]))

