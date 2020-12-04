import copy  # copy module is used to cleanly create a deep copy of nested lists

# grid rows used to create 2d array for game grid
top_row = [" ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 "]
first_row = ["1", "-", "-", "-", "-", "-"]
second_row = ["2", "-", "-", "-", "-", "-"]
third_row = ["3", "-", "-", "D", "D", "-"]  # Destroyer is hiding in this row, shown as 'D'
fourth_row = ["4", "-", "-", "-", "-", "-"]
fifth_row = ["4", "-", "-", "-", "-", "-"]

grid = [top_row, first_row, second_row, third_row, fourth_row, fifth_row]  # 2d list containing the game grid

display_grid = copy.deepcopy(grid)  # deepcopy to get a copy of nested elements to stop them being mutated in grid list

finished = False  # used to control the non-deterministic game loop


# function used to print the grid whenever its called
def display(first_input=-1, second_input=-1):
    for row_index, row in enumerate(display_grid):  # loop through each row
        for column_index, item in enumerate(row):  # loop through each item in the row
            if item not in ["1", "2", "3", "4", "5", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", "[H]", "[M]", " "]:
                # if the item doesnt equal a H (Hit), M (Miss) or a number, then make it a space
                display_grid[row_index][column_index] = "[ ]"
        print(*row, sep=" ")  # remove the list brackets and quotation marks


# function used to ensure users give valid inputs
def user_selection(position):
    user_input = ""  # ensure user_input is cleared
    while True:  # while loop ensures user gives a valid input
        try:
            user_input = int(input("Enter {} number: ".format(position)))
            if user_input < 1 or user_input > 5:  # if number out of range
                print("try again, ensure integer is between 1-5")
                continue  # go back to the start of the while loop
            else:  # correct input
                break  # leave the loop and return the valid input
        except ValueError:  # if not a valid integer, ask for an integer
            print("please enter an integer between 1 and 5")
    return user_input  # return the value to store in input variable


# function checks to see if the shot is a hit or a miss based on the parameters provided
def hit_check(col, row):
    if grid[col][row] == "D":  # if we get the Destroyer, its a hit
        display_grid[col][row] = "[H]"
        display()
        print("Well done you hit!")
    else:
        display_grid[col][row] = "[M]"
        display()
        print("Sorry you missed.")


# function checks to see if the game has been completed
def finish_check():
    global finished  # need the global finished variable so we can break out of the game loop
    hit_counter = 0  # used to check if we manage to find two hits inside the list
    for row in display_grid:  # loop through each row
        for item in row:  # loop through each item in the row
            if item == "[H]":  # if item is an 'H' its  been hit
                hit_counter += 1  # add one to the counter as an 'X' is found
    if hit_counter == 2:  # if we have hit twice, destroyer is sunk
        print("Glug, glug, glug... you won.")  # winning message!
        finished = True  # breaks the game loop, ending the game


# intro text - only displayed once to user so kept outside the loop
print("\nWelcome to Battleships!")
print("\nThe Destroyer is lurking out there, enter coordinates to take a shot and try to sink it\n")
display()

while not finished:  # continuous game loop until broken
    # first coordinate selection
    print("\nEnter the coordinates for your shot!")
    first_user_input = user_selection("row")
    second_user_input = user_selection("column")
    print("\n")
    # if position has already been shot at, don't shot again
    if display_grid[first_user_input][second_user_input] == "[H]" or \
            display_grid[first_user_input][second_user_input] == "[M]":
        print("\nThis location has already been tried, please shoot again!\n")
        continue  # go back to the top of the loop
    hit_check(first_user_input, second_user_input)

    # check to see if the game was been completed
    finish_check()  # if game is finished, function breaks the while loop, ending the program


