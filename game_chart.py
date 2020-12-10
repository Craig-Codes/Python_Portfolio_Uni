from tabulate import tabulate  # import tabulate to help draw nice tables


# Class is used to create the game template, and hold the necessary information
class Game:
    def __init__(self, title, publisher, sales):
        self.title = title
        self.publisher = publisher
        self.sales = sales


# store menu choices in a list for easy data retrieval and manipulation
menu_choices = ["1. Enter new game details", "2. Update game sales figures",
                "3. Remove Game", "4. Print chart", "5. Quit"]

game_list = []  # list stores all of the games


# function ensures input is legitimate
def input_choice():
    while True:
        try:
            chosen_input = int(input(": "))
            if chosen_input in (1, 2, 3, 4, 5):  # check to ensure input is a valid choice
                break  # valid input so break the loop and return users input
            else:
                print("Enter a valid number to make a selection\n")
        except ValueError:  # input isn't a valid integer
            print("Enter a valid number to make a selection\n")

    return chosen_input  # return the valid selection


# function controls which functions are triggered based on user input
def input_action(choice):
    if choice == 1:
        new_game()
    elif choice == 2:
        update_sales()
    elif choice == 3:
        remove_game()
    elif choice == 4:
        top_five_print()  # sorts the top 5 then prints the table
    if choice == 5:
        exit()  # exit the program


# function creates a new game
def new_game():
    title = input("Enter the game title: ")
    publisher = input("Enter the publisher: ")
    while True:  # loop to ensure sales given correctly
        try:
            sales = int(input("Enter the sales: "))
            break  # valid input, break the loop
        except ValueError:
            print("Ensure you enter a valid numeric answer")
    game = Game(title, publisher, sales)  # create the game with user inputs
    game_list.append(game)  # add the game to the games list
    print("\nNew game, titled '{}' has been created!\n".format(title))


# function updates chosen game sales
def update_sales():
    game_found = False  # flag used to check if any game title was found
    name = input("Enter the game's title to select it: ")
    while True:  # loop to ensure sales given correctly
        try:
            sales = int(input("Enter the games updated sales figure: "))
            break  # valid input, break the loop
        except ValueError:
            print("Ensure you enter a valid numeric answer")

    # loop through the games in the games_list, if the title matches, update that games sales
    for game in game_list:
        if game.title.lower() == name.lower():  # make both strings lowercase to remove case sensitivity issues
            game.sales = sales
            print("\nthe sales for {} have been updated to {}\n".format(game.title, game.sales))
    if not game_found:
        print("\nNo game of title '{}' found!\n".format(name))


# function removes the chosen game from the list
def remove_game():
    game_found = False  # flag used to check if any game title was found
    name = input("Enter the game's title to remove it: ")
    for game in game_list:
        if game.title.lower() == name.lower():  # make both strings lowercase to remove case sensitivity issues
            game_list.remove(game)
            game_found = True
            print("\n{} has been removed!\n".format(game.title))
    if not game_found:
        print("\nNo game of title '{}' found!\n".format(name))


# function sorts list into top five then prints the data
def top_five_print():
    from operator import attrgetter  # attribute getter
    # sort the list from highest to lowest based on the sales key in the objects
    sorted_list = sorted(game_list, key=lambda x: x.sales, reverse=True)
    top_five_sorted = sorted_list[:5]  # take the first 5 entries from the sorted list

    # make the table
    headings = ["Position", "Game Title", "Publisher", "No. of Sales"]  # table headers
    table = [[1, top_five_sorted[0].title, top_five_sorted[0].publisher,
              top_five_sorted[0].sales],
             [2, top_five_sorted[1].title, top_five_sorted[1].publisher,
              top_five_sorted[1].sales],
             [3, top_five_sorted[2].title, top_five_sorted[2].publisher,
              top_five_sorted[2].sales],
             [4, top_five_sorted[3].title, top_five_sorted[3].publisher,
              top_five_sorted[3].sales],
             [5, top_five_sorted[4].title, top_five_sorted[4].publisher,
              top_five_sorted[4].sales],
             ]

    print(tabulate(table, headings, tablefmt="fancy_grid"))  # build the table using headings and content


# generate the games
cyberpunk = Game("Cyberpunk 2077", "CDPR", 1000000000)
game_list.append(cyberpunk)  # add generated game to the game list
minecraft = Game("Minecraft", "Monjang Studios", 200000000)
game_list.append(minecraft)
gta5 = Game("GTAV", "Rockstar North", 135000000)
game_list.append(gta5)
pacman = Game("Pac-Man", "Namco", 39498000)
game_list.append(pacman)
tlou = Game("The Last of Us", "Naughty Dog", 20000000)
game_list.append(tlou)

# create the menu system
while True:  # loop ensuring user remains in the program until 'exit' is chosen
    print("Please select which action you would like to take\n")
    # display the menu option
    for entry in menu_choices:
        print(entry)
    user_input = input_choice()
    input_action(user_input)
