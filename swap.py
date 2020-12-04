# Method get user number inputs, ensuring they are valid
def int_input():
    while True:  # loop ensures an input
        try:
            user_input = int(input(": "))
            break  # valid input so leave the loop
        except ValueError:
            print("Please enter an integer")
            continue  # go back to top of loop to try and get a valid input again
    return user_input


def print_int_list():
    print(*number_list, sep=" ")  # print the list without brackets, separated with a space between each entry


def swap():  # method swaps the list entries using a placeholder as temporary storage
    holder = number_list[0]
    number_list[0] = number_list[1]
    number_list[1] = holder


print("Please give the first number")
first_input = int_input()
print("\nPlease give the second number")
second_input = int_input()

number_list = [first_input, second_input]
print("\nYou entered:")
print_int_list()
swap()
print("Your entries swapped:")
print_int_list()
