number_list = []


# Method get user number inputs, ensuring they are valid
def int_input():
    while len(number_list) < 5:  # loop ensures we get 5 number inputs from the user
        try:
            user_input = int(input(": "))
            number_list.append(user_input)
        except ValueError:
            print("Please enter an integer")
            continue  # go back to top of loop to try and get a valid input again


# function sorts the number list into descending order
def sort():
    # loop through each list entry
    for i in range(1, len(number_list)):  # we want to start the range at 1, as the left most item doesnt need to be in
        # the sorting list as there is no item to its left - get all the values after the first one
        # looping through each value in the list, except the first value
        value = number_list[i]  # value is taken into the 'sorted' sub-list, and is compared to first value(j)
        j = i - 1  # this always refers to the item to the left of the current item we are looking at
        while j >= 0 and number_list[j] < value:
            # if value to the left if lower than the value we are trying to sort, switch the numbers around
            #  j >= 0 stops negative indexing
            number_list[j + 1] = number_list[j]
            j -= 1
        number_list[j + 1] = value  # we have swapped the two values around


print("Please enter 5 integers, so that the program can arrange them in descending order")
int_input()
sort()
print("\nThe list sorted into descending order is:")
print(*number_list, sep=" ")



