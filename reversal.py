
def reverse_int(user_int):  # function reverses the user input integer
    reverse_number = 0  # reverse number needs to start off as 0, so placed outside the while loop
    while user_int > 0:  # loop continues whilst the user input integer is greater than 0
        remainder = user_int % 10  # modulo 10 pulls out the rightmost number
        reverse_number = (reverse_number * 10) + remainder  # reversed_number appends the remainder
        user_int = user_int // 10  # // gives integer division not floating point division.
        # Dividing by 10 removes the rightmost number before the next loop starts
    print("Reverse of the provided number is {}".format(reverse_number))


while True:  # is_running variable controls the non-deterministic loop
    try:  # try to convert input into an integer
        user_input = int(input("Enter an integer of at least 2 digits or -1 to quit: "))
    except ValueError:  # if input not an integer
        print("Your input is invalid, please try again.")
        continue  # break out of current loop iteration and re-try input

    if user_input == -1:
        print("Program end.")
        break  # break from the loop, exiting the program
    elif user_input < 1:  # input is less than 1, so zero or a minus number
        print("Your input is invalid, please try again.")
        continue  # break out of current loop iteration and re-try input
    elif len(str(user_input)) < 2 or len(str(user_input)) > 10:
        # if less than 2 characters in the user input or more than 11
        print("Your input is invalid, please try again.")
        continue  # break out of current loop iteration and re-try input
    else:  # legitimate valid input
        reverse_int(user_input)  # function prints the reversed integer value
        break  # input has been accepted and processed by function, so break out of the loop to end program
