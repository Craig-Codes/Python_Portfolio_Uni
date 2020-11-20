from random import choice  # module function gets a random choice from a list of values

choice_tuple = ("paper", "rock", "scissors")  # list of possible values the computer can choose from

player_score = 0  # start player and computer scores at zero
computer_score = 0


def input_choice():
    while True:  # loop ensures we get a correct answer before returning
        user_input = input("Enter your selection: ")
        if user_input.lower() not in choice_tuple:  # if case insensitive input isn't a valid choice
            print("Please type either 'paper', 'rock' or 'scissors'")  # user given input information
            continue  # break loop iteration and re-try
        elif user_input.lower() in choice_tuple:  # valid input
            break  # break from the loop and return the value

    return user_input.lower()  # return a valid user input


def game_result(user_guess, computer_guess):
    global player_score, computer_score  # access global scores
    if user_guess == "rock":
        if computer_guess == "paper":
            computer_score += 1
            print("The computer won.")
        elif computer_guess == "rock":
            print("It was a draw.")
        else:
            print("Congratulations, you win")
            player_score += 1
    elif user_guess == "paper":
        if computer_guess == "scissors":
            computer_score += 1
            print("The computer won.")
        elif computer_guess == "paper":
            print("It was a draw.")
        else:
            print("Congratulations, you win")
            player_score += 1
    elif user_guess == "scissors":
        if computer_guess == "rock":
            computer_score += 1
            print("The computer won.")
        elif computer_guess == "scissors":
            print("It was a draw.")
        else:
            print("Congratulations, you win")
            player_score += 1


while True:  # while loop controls the game loop
    user_selection = input_choice()
    print("You chose: {}".format(user_selection).capitalize())
    computer_choice = choice(choice_tuple)
    print("The computer chose: {}".format(computer_choice).capitalize())
    game_result(user_selection, computer_choice)  # function checks to see who wins round based on the input

    # check to see if anyone has won the game
    if player_score == 3:
        print("Well done the game well done!")
        break  # break the loop to finish the game
    elif computer_score == 3:
        print("Commiserations the computer won...\nGame over...")
        break
    else:  # output current scores then enter next loop iteration
        print("You need: {} to complete the game".format(3 - player_score))  # take the score from winning total of 3
        print("The computer needs: {} to complete the game".format(3 - computer_score))
        print("************************************************")
