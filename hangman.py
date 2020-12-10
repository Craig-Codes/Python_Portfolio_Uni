guessed_letters = []  # list to store all of users letter guesses
guessed_word = ""  # variable holds the guessed word
guess_counter = 0  # variable stores the guess counter

# function masks the word if letter hasn't been guessed yet
def word_mask():
    global guessed_word  # guessed word always starts blank, its then populated with letters by for loop
    guessed_word = ""
    for entry in word_letters:  # loop through each character in the word_letter array
        if entry in guessed_letters:  # loop though all of the letters a user has guessed
            # If a letter matches, the letter is concatenated to the guessed_word variable
            guessed_word += entry
        else:
            # If a letter isn't found, a '-' is concatenated to the guessed_word variable
            guessed_word += "-"


word_to_guess = input("Enter the word which needs to be guessed: ")
word_letters = list(word_to_guess)  # create a list of all the word letters
word_mask()  # mask the game word

while True:  # game loop
    guess_counter += 1  # each loop iteration adds one to the guess counter
    print("\nYour word to guess is {}\n".format(guessed_word))
    letter = input("Enter a letter to guess the word: ")
    guessed_letters.append(letter)  # add the letter to the guessed_letters list
    word_mask()
    # check to see if game is over
    if guessed_word == word_to_guess:
        print("\nWell done you have successfully guessed the word!")
        print("You took {} guesses to successfully guess the word '{}'".format(guess_counter, word_to_guess))
        break  # leave the loop and stop the program


