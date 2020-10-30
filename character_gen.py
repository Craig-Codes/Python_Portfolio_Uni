import random  # import random module
from tabulate import tabulate  # import tabulate to help draw nice tables

creation_in_progress = True  # variable starts True, if changes to false program ends and user has a character

# Add character class base attributes to dictionaries
warrior = {"strength": 15,
           "intelligence": 0,
           "wisdom": 0,
           "dexterity": 12,
           "constitution": 10}

wizard = {"strength": 0,
          "intelligence": 15,
          "wisdom": 10,
          "dexterity": 10,
          "constitution": 0}

thief = {"strength": 10,
         "intelligence": 9,
         "wisdom": 0,
         "dexterity": 15,
         "constitution": 0}

necromancer = {"strength": 10,
               "intelligence": 10,
               "wisdom": 15,
               "dexterity": 0,
               "constitution": 0}

# Create the deficit and surplus values
deficit = {"strength": 0,
           "intelligence": 0,
           "wisdom": 0,
           "dexterity": 0,
           "constitution": 0}

surplus = {"strength": 0,
           "intelligence": 0,
           "wisdom": 0,
           "dexterity": 0,
           "constitution": 0}

# randomise player scores
strength = random.randint(3, 18)
intelligence = random.randint(3, 18)
wisdom = random.randint(3, 18)
dexterity = random.randint(3, 18)
constitution = random.randint(3, 18)

player = {"strength": strength, "intelligence": intelligence,
          "wisdom": wisdom, "dexterity": dexterity, "constitution": constitution}

# tuple holding all possible attributes
attributes_tuple = ("strength", "intelligence", "wisdom", "dexterity", "constitution")


# function calculates deficit values
def deficit_calculator(player_score, character_score):
    score = player_score - character_score
    return score


# function calculates surplus values
def surplus_calculator(player_score, character_score):
    score = player_score - character_score  # take the player score from the character score to get the surplus value
    if character_score > 3 and player_score > 3:
        return score
    elif character_score <= 3:
        return score - 3


# function creates the player stats table
def table_creator(character, character_name):
    attributes = ["strength", "intelligence", "wisdom", "dexterity", "constitution"]
    player_scores = (player["strength"], player["intelligence"],
                     player["wisdom"], player["dexterity"], player["constitution"])

    for i in range(len(attributes)):
        attribute = attributes[i]  # get attribute value from attributes list
        players_attribute_score = player_scores[i]  # get player scores from player_scores list
        if players_attribute_score > character[attribute]:
            # if players_score is greater than the character classes minimum required score - add to surplus
            surplus[attribute] = surplus_calculator(players_attribute_score, character[attribute])
        elif players_attribute_score < character[attribute]:
            # if players_score is less than the character classes minimum required score - add to deficit
            deficit[attribute] = deficit_calculator(players_attribute_score, character[attribute])

    # create "-" from 0 entrys before popualting the table
    # copy player dictionary into a new dictionary and loop though setting 0 values to "-"
    player_dict = dict(player)
    for key, score in player_dict.items():
        if score == 0:
            player_dict[key] = "-"
        else:
            score = int(score)

    base_dict = dict(character)
    for key, score in base_dict.items():
        if score == 0:
            base_dict[key] = "-"
        else:
            score = int(score)

    deficit_dict = dict(deficit)
    for key, score in deficit_dict.items():
        if score == 0:
            deficit_dict[key] = "-"
        else:
            score = int(score)

    surplus_dict = dict(surplus)
    for key, score in surplus_dict.items():
        if score == 0:
            surplus_dict[key] = "-"
        else:
            score = int(score)

    headings = ["Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]  # table headers

    table = [["Base Score", player_dict["strength"], player_dict["intelligence"],
              player_dict["wisdom"], player_dict["dexterity"], player_dict["constitution"]],
             [character_name, base_dict["strength"], base_dict["intelligence"], base_dict["wisdom"],
              base_dict["dexterity"], base_dict["constitution"]],
             ["Deficit", deficit_dict["strength"], deficit_dict["intelligence"], deficit_dict["wisdom"],
              deficit_dict["dexterity"], deficit_dict["constitution"]],
             ["Surplus", surplus_dict["strength"], surplus_dict["intelligence"], surplus_dict["wisdom"],
              surplus_dict["dexterity"], surplus_dict["constitution"]]
             ]

    print(tabulate(table, headings, tablefmt="fancy_grid"))  # create the table using headings and content


# function checks to see if we have any values inside the deficit dictionary
def finish_check():
    global creation_in_progress
    deficit_check_list = []  # empty list used to add any found deficits
    for attribute, value in deficit.items():
        # loop though deficit dictionary, appending values over 0 to the list
        if value < 0:
            deficit_check_list.append(attribute)

    if len(deficit_check_list) == 0:
        creation_in_progress = False  # closes final while loop, finishing the application


# function works out if the surplus can actually be used to make up deficit based on 2 to 1 exchange ratio
def deficit_surplus_calculation():
    surplus_score = surplus["strength"] + surplus["intelligence"] + surplus["wisdom"] \
                    + surplus["dexterity"] + surplus["constitution"]

    deficit_score = deficit["strength"] + deficit["intelligence"] \
                    + deficit["wisdom"] + deficit["dexterity"] + deficit["constitution"]

    # if the deficit multiplied by 2 is not greater than the surplus score,
    # player doesnt have enough points to be character
    # deficit score multiplied by -1 to turn it into a plus score first
    deficit_score_plus = deficit_score * -1
    if deficit_score_plus * 2 > surplus_score:
        print("Unfortunately you do not have enough points to exchange to become this character!")
        print("Please try again")
        exit()
    finish_check()

    print("\nYou have {} points to exchange".format(surplus_score))
    print("You can trade points from non-required attributes at the rate of 2 to 1")


print("Welcome to the Character Generator")
print("\nThe character types are: ")
character_classes = ("warrior", "wizard", "thief", "necromancer")  # tuple storing possible classes
print("Warrior, Wizard, Thief, Necromancer")  # use * to remove the tuple brackets, and separate each entry with a comma

while True:  # while loop to ensure we get a valid selection
    character_type = str(input("\nChoose a character type from the above list by typing its name: ")).lower()
    if character_type in character_classes:  # lower to remove case sensitivity
        break  # break the loop allowing user to move on
    else:
        print("Error, select again! Ensure you spell the character correctly.")

# Create table output based on users character selection
if character_type == "warrior":
    table_creator(warrior, "Warrior")
elif character_type == "wizard":
    table_creator(wizard, "Wizard")
elif character_type == "thief":
    table_creator(thief, "Thief")
elif character_type == "necromancer":
    table_creator(necromancer, "Necromancer")

finish_check()  # check to see if character meets all minimum requirements

# while loop ensures player keeps being prompted to amend attributes until character created
while creation_in_progress:
    # calculate the total amount of surplus and deficit - tell user if possible to have
    deficit_surplus_calculation()

    while True:  # loop to ensure user provides correct input
        print("which attribute would you like to take points from?")
        chosen_attribute = input("type attribute name: ").lower()
        if chosen_attribute in attributes_tuple:
            break
        else:
            print("attribute not recognised")

    while True:  # loop to ensure user provides correct input
        try:
            points_taken = int(input("how many points would you like to take? "))
            if points_taken % 2 == 0:  # ensure number is divisible by 2
                if surplus[chosen_attribute] - points_taken < 0:
                    print("you cannot take that many points")
                else:
                    break
            else:
                print("points are exchanged 2 to 1, you need to exchange an even number of points")

        except ValueError:
            print("ensure you type a number")

    while True:
        print("which attribute would you like to give points to? ")
        swap_attribute = input("type attribute name: ").lower()
        if swap_attribute in attributes_tuple:
            break

    if character_type == "wizard":
        player[chosen_attribute] -= int(points_taken)
        surplus[chosen_attribute] -= int(points_taken)
        player[swap_attribute] += int(points_taken / 2)
        deficit[swap_attribute] += int(points_taken / 2)
        table_creator(wizard, "Wizard")
    elif character_type == "thief":
        player[chosen_attribute] -= int(points_taken)
        surplus[chosen_attribute] -= int(points_taken)
        player[swap_attribute] += int(points_taken / 2)
        deficit[swap_attribute] += int(points_taken / 2)
        table_creator(thief, "Thief")
    elif character_type == "necromancer":
        player[chosen_attribute] -= int(points_taken)
        surplus[chosen_attribute] -= int(points_taken)
        player[swap_attribute] += int(points_taken / 2)
        deficit[swap_attribute] += int(points_taken / 2)
        table_creator(necromancer, "Necromancer")
    elif character_type == "warrior":
        player[chosen_attribute] -= int(points_taken)
        surplus[chosen_attribute] -= int(points_taken)
        player[swap_attribute] += int(points_taken / 2)
        deficit[swap_attribute] += int(points_taken / 2)
        table_creator(warrior, "Warrior")

    finish_check()  # check to see if character meets all minimum requirements

print("character successfully created!")
print("\nhere's your character:")

# create "-" from 0 entry's before populating the table
# copy player dictionary into a new dictionary and loop though setting 0 values to "-"
player_final_dict = dict(player)
for key, score in player_final_dict.items():
    if score == 0:
        player_final_dict[key] = "-"
    else:
        score = int(score)

headings = ["Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]  # table headers

table = [["Your Character", player["strength"], player["intelligence"],
          player["wisdom"], player["dexterity"], player["constitution"]]]

print(tabulate(table, headings, tablefmt="fancy_grid"))
