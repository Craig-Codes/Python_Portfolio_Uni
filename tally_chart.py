# lists store candidates and their vote tallies
craig = ["Craig", 0]
karen = ["Karen", 0]
diane = ["Diane", 0]
steven = ["Steven", 0]
leanne = ["Leanne", 0]


# function displays all candidate names
def show_candidates():
    candidates = ["Craig", "Karen", "Diane", "Steven", "Leanne"]
    candidate_numbers = [2, 3, 4, 5, 6]
    for i in range(5):
        print("{}. {}".format(candidate_numbers[i], candidates[i]))


# function gets user input
def vote():
    while True:  # make sure we get a valid number input
        try:
            candidate_no = float(input("\nEnter the candidates number: "))
            if candidate_no in (1, 2, 3, 4, 5, 6):  # tuple containing valid number inputs
                break  # valid number so break and return the number
            else:
                print("Enter a number between 1 and 6")
        except ValueError:
            print("Invalid input, Enter a number between 1 and 6")
    return candidate_no


# function displays results, showing the winner
def results():
    candidate_tally = [craig, karen, diane, steven, leanne]
    sorted_list = []
    for candidate in candidate_tally:  # loop through the list of lists
        # add item to the end of the sorted list - ensures sorted_list always has an entry
        sorted_list.append(candidate)  # if candidate has the least votes, this isnt popped off and is in correct place
        for i in range(len(sorted_list)):  # loop over each item in the sorted list
            # if the candidate votes are greater than the current candidate,
            # add the item to the list before that current entry using the insert method
            if candidate[1] > sorted_list[i][1]:  # compare the current candidate votes against the sorted list votes
                sorted_list.insert(i, candidate)  # insert method adds entry at specified index where votes were higher
                sorted_list.pop()  # found the item and inserted it, so can pop off the end to avoid double entries
                break  # leave the loop as entry has been added
    for item in sorted_list:
        print("{} - {} votes".format(item[0], item[1]))


# function adds vote to the selected candidate:
def add_vote(candidate):
    if candidate == 2:
        craig[1] += 1
    elif candidate == 3:
        karen[1] += 1
    elif candidate == 4:
        diane[1] += 1
    elif candidate == 5:
        steven[1] += 1
    elif candidate == 6:
        leanne[1] += 1


print("Please select the candidate you wish to vote for from the bellow list, by typing in the candidates number")
print("To finish voting and see the results type '1'\n")

while True:
    show_candidates()
    candidate = vote()  # get the number input from the user
    if candidate == 1:
        results()
        break  # leave the loop ending the program
    add_vote(candidate)  # function adds the vote to the relevant candidate
