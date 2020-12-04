# Program prints a character a specified number of times

while True:  # loop ensuring we get an input
    character = str(input("Enter the character you would like to be repeated: "))
    if len(character) > 1:  # if character length is greater than one, its not a single character
        print("Please type in a single character")
    else:
        break  # we have a valid character, so break the loop

while True:  # loop ensuring we get an input
    try:
        number = int(input("Enter the number of times you want to repeat the character: "))
        if number < 1:
            print("Please enter a positive integer")
            continue  # restart the loop to get a valid input
        else:
            break  # break from the loop
    except ValueError:  # if input isn't a valid integer
        print("Please enter a valid integer")
        continue  # restart the loop to get a valid input


def print_character(character_choice, number_choice):
    print(character_choice * number_choice)


print_character(character, number)