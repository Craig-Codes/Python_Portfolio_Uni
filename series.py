# variables storing running totals
positive_total = 0
negative_total = 0


# function used to take user input and add to total variables
def user_input():
    global positive_total, negative_total # Get access to the global variables
    number = int(input("Enter a positive or negative integer: "))
    if number >= 1:
        positive_total += number  # add current positive_total to the input number
    else:
        negative_total += number


# loop 5 times, calling the user_input function each time
for iteration in range(5): # range is 0 - 5 exclusive of 5 (the stopping point)
    user_input()


# output the users inputs added together
print("Sum of positive integers: {}".format(positive_total))
print("Sum of negative integers: {}".format(negative_total))
