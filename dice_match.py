import random  # random module used to easily generate a random number in a range

role_counter = 0  # variable stores the number of dice rolls
matched = False  # variable controls the loop, only stopping when dice rolls match

while not matched:
    role_counter += 1  # always increment the tole counter by one
    dice_one = random.randint(1, 6)  # generate a random number 1 to 6
    print("Dice one rolled a {}".format(dice_one))
    dice_two = random.randint(1, 6)  # generate a second random number 1 to 6
    print("Dice two rolled a {}".format(dice_two))
    print("--------------------\n")  # line to break up each role for readability

    if dice_one == dice_two:
        print("It took {} throws for the dice to match!".format(role_counter))
        break
