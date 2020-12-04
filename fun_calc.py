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


# Method gets user operator input, ensuring its a valid selection
def op_input():
    while True:  # loop ensures an input
        try:
            user_input = int(input(": "))
            if user_input in (1, 2, 3, 4, 5):  # Check to see if input is in the valid number range tuple
                break  # valid input
            else:
                print("Please enter an integer (1-5)")
                continue
        except ValueError:
            print("Please enter an integer (1-5")
            continue  # go back to top of loop to try and get a valid input again
    return user_input


def add():
    answer = first_input + second_input
    print("{} + {} = {}".format(first_input, second_input, answer))


def subtract():
    answer = first_input - second_input
    print("{} - {} = {}".format(first_input, second_input, answer))


def multiply():
    answer = first_input * second_input
    print("{} * {} = {}".format(first_input, second_input, answer))


def divide():
    try:
        answer = first_input / second_input
        print("{} / {} = {}".format(first_input, second_input, answer))
    except ZeroDivisionError:
        print("{} / {} = 0".format(first_input, second_input))  # default the answer of a zero division to zero


def remainder():
    answer = first_input % second_input
    print("{} % {} = {}".format(first_input, second_input, answer))


print("Please give the first number of the calculation")
first_input = int_input()
print("\nPlease give the second number of the calculation")
second_input = int_input()

operators = ("1. Add", "2. Subtract", "3. Multiply", "4. Divide", "5. Remainder")  # tuple of operators
print("\nPlease select which operation to perform on the input's (1-5)")
for operator in operators:  # loop through tuple and display options line by line
    print(operator)

operator_input = op_input()
if operator_input == 1:  # selected add
    add()
elif operator_input == 2:  # selected subtract
    subtract()
elif operator_input == 3:  # selected multiply
    multiply()
elif operator_input == 4:  # selected divide
    divide()
elif operator_input == 5:  # selected remainder
    remainder()
