password_list = []  # list stores all passwords


# function takes in users menu input, ensuring a correct input is returned
def selection_input():
    while True:  # loop ensures a valid input is entered before moving on
        try:  # try / except block used to ensure correct input
            user_input = int(input("Please enter 1 for new user, or 2 for an existing user: "))
            if user_input not in (1, 2):  # if user input is not 1 or 2
                print("You have entered an invalid input")
            else:
                break  # input is either 1 or 2 so valid
        except ValueError:
            print("You have entered an invalid input")
    return user_input  # return the users input


# function checks the new passwords match
def password_checker(password):
    print("Please re-enter the password to confirm it")
    re_enter = input(":")
    if re_enter == password:
        print("\n*** The passwords match, new entry created! ***\n")
        password_list.append(password)  # add new password to the password list
    else:
        print("*** Passwords do not match, new entry not created! ***\n")


# function creates the new user, ensuring password conditions are met
def new_user_creation():
    while True:  # ensure user gives a password
        print("The password must be at least 8 characters long, it cannot begin, end or contain a space, "
              "and cannot begin with a number.")
        password = input(":")

        # check password is at least 8 characters long
        if len(password) > 8:
            first_letter = password[0]  # we know we can get the first index now, as over 8 characters in the input
        else:
            print("Password is less than eight characters")
            continue  # go to the top of the loop

        # check password doesnt contain a space
        if ' ' not in password:
            pass  # nothing has to happen, just pass over if/else block
        else:
            print("Password contains a space")
            continue

        # check password doesnt begin with a number
        if not first_letter.isnumeric():  # if first letter is a number, start again
            break  # all conditions have been met, leave the loop
        else:
            print("Password must not start with a numeric character")
    password_checker(password)  # function checks the new valid input passwords match to confirm new password


# function checks user input password against passwords stored in the passwords_list
def existing_user_login():
    attempts = 0  # keep track of number of password attempts
    while True:  # loop to control login attempts
        if len(password_list) == 0:  # if no passwords in the list, return to the menu
            print("Sorry, no passwords have been set, please create a new entry...")
            print("\nCreate a new password!\n")
            new_user_creation()
            break  # break out of the loop, returning to the menu
        elif attempts == 3:  # check if password has been guessed 3 times
            print("\n***** Password entered incorrectly 3 times, password locked out *****\n")
            break  # break the loop
        else:
            attempts += 1
            print("Enter your password")
            existing_password = input(": ")
            if existing_password in password_list:
                print("\n***** Password accepted, welcome! *****\n")
                break  # break the loop
            else:  # remain in the loop
                print("Password didn't match... You've had {} attempts of 3".format(attempts))


print("\nWelcome to the password protected entry system\n")

while True:  # program loop to keep user in the menu system after inputs
    user_selection = selection_input()
    if user_selection == 1:
        print("\nCreate a new password!\n")
        new_user_creation()
    elif user_selection == 2:
        existing_user_login()
