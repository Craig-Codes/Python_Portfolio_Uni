from tabulate import tabulate  # import tabulate to help draw nice tables

number_of_ratings = 0  # counter stores the number of times we get a rating
ratings = []  # empty list to store the ratings
ratings_totals = []  # empty list stores the amount of each number found


# function ensures input is legitimate and adds all inputs to the ratings list
def input_choices():
    global number_of_ratings
    while True:  # while loop ensures we keep getting ratings until user enters -1
        try:
            chosen_input = int(input(": "))
            if chosen_input in (1, 2, 3, 4, 5):  # check to ensure input is a valid choice against tuple
                number_of_ratings += 1  # increment the number of ratings by 1
                ratings.append(chosen_input)  # add rating to the input list
            elif chosen_input == -1:
                print("Ratings input has finished!\n")
                break  # leave the input loop
            else:
                print("Number out of range, enter 1 - 5\n")
        except ValueError:  # input isn't a valid integer
            print("Enter a valid number (1-5) to make a selection\n")


# function creates a list storing how many times each number was selected, for use in the output table
def table_values():
    # variables used to store the amount of each number found in the ratings list
    global ratings_totals
    one = two = three = four = five = 0  # start all variables at value 0
    for rating in ratings:  # each time a value is found, add one two its corresponding variable
        if rating == 1:
            one += 1
        elif rating == 2:
            two += 1
        elif rating == 3:
            three += 1
        elif rating == 4:
            four += 1
        elif rating == 5:
            five += 1
    ratings_totals = [one, two, three, four, five]  # store the amount of each value in a list


# function outputs the values in a table, showing the amount of times each rating was given, and the average rating
def table_builder():
    global ratings_totals, number_of_ratings
    try:  # try / catch block used to catch zero division errors if no ratings are given
        total = (ratings_totals[0] * 1) + (ratings_totals[1] * 2) + (ratings_totals[2] * 3) \
                + (ratings_totals[3] * 4) + (ratings_totals[4] * 5)
        average = total / number_of_ratings

        # table setup
        headings = ["Ratings", "Total"]  # table headers
        table = [["1", ratings_totals[0]],
                 ["2", ratings_totals[1]],
                 ["3", ratings_totals[2]],
                 ["4", ratings_totals[3]],
                 ["5", ratings_totals[4]],
                 ["Average", average]]

        print(tabulate(table, headings, tablefmt="fancy_grid"))  # build the table using headings and content

    except ZeroDivisionError:  # if no input 0/0 will cause a zero division error
        print("Sorry, unable to workout a total with no ratings")


print("\nWelcome the Rate a Restaurant!\n")
print("Please rate the restaurant 1 - 5 (1 is very poor, 5 is excellent)\n")
print("Enter '-1' to finish data input\n")
input_choices()  # function loops until user finishes putting in all inputs
table_values()  # function calculates how many of each rating is contained in the ratings list
table_builder()  # function creates the table showing amount each value is entered, and the average
