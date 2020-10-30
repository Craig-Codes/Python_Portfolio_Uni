# A program to prompt the user to enter a number between 1 and 4 inclusive, before out putting a thunderbird.

# function to prompt user for input, cleanly dealing with input errors
def number_input():
    global selected_number
    try:
        user_input = int(input("Type a whole number between 1 and 4: "))  # get user input
        return user_input
    except ValueError:
        # if entered value isn't a number, catch the error and try again
        print("Please ensure you type a number")
        return number_input()  # recursively call the function again to get user to input another value


selected_number = number_input()  # call the function to get user input at the start of the program
valid_numbers = (1, 2, 3, 4)  # tuple to store valid numbers

if selected_number in valid_numbers:
    if selected_number == 1:
        print("Thunderbird 1 pilot is Scott Tracy")
    elif selected_number == 2:
        print("Thunderbird 2 pilot is Virgil Tracy")
    elif selected_number == 3:
        print("Thunderbird 3 pilot is Alan Tracy")
    elif selected_number == 4:
        print("Thunderbird 4 pilot is Gordon Tracy")
else:
    print("Have you never watched Thunderbirds!")






