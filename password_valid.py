password = "Rocket"
user_guess = str(input("Please enter the password: "))

#  use the .lower() method on both variables to get rid of case sensitivity, and compare the variables
if password.lower() == user_guess.lower():
    print("Welcome!")
else:
    print("Access Denied")
