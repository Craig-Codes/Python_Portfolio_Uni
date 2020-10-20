import random

# list of all possible cards
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# generate a random number between 0 and 12 inclusive
random_number = random.randint(0, 12)

# use the random number to get the position in the list, getting a random corresponding card
dealt_card = cards[random_number]
print("Welcome to the higher or lower card game! Aces are low and repeated cards are always incorrect, sorry!")
print("Card dealt is: " + dealt_card)

# get the user input, either h/l for higher or lower
higher_or_lower = str(input("Will the next card be higher or lower? (h/l) ")).lower()

random_second_number = random.randint(0, 12)  # generate a second random number
dealt_second_card = cards[random_second_number]  # get a second card using random number as list index
print("Second card dealt is: " + dealt_second_card)

# if / else statement to let user know if they guessed correctly or not
if higher_or_lower == "h":
    if cards.index(dealt_card) < cards.index(dealt_second_card):
        print("Card was higher, you win!")
    else:
        print("Card was lower, you lose!")
elif higher_or_lower == "l":
    if cards.index(dealt_card) > cards.index(dealt_second_card):
        print("Card was lower, you win!")
    else:
        print("Card was higher, you lose!")
else:
    print('Try again ensuring you type "h" for higher or "l" for lower')