input_count = 0  # stores number of user inputs
positive_inputs = 0  # stores value of all positive integers
negative_inputs = 0  # stores value of all negative integers
positive_counter = 0  # keep track of number of positive numbers entered by user
negative_counter = 0  # keep track of number of negative numbers entered by user

while input_count < 10:  # loop 10 times - while loop chosen as loop may run over 10 times to account for input errors
    try:
        input_int = int(input("Enter a positive or negative integer value: "))
        input_count += 1  # add 1 to input count - once at 10 loop while breaks
        if input_int > 0:  # if input is greater than zero, its a positive integer
            positive_counter += 1
            positive_inputs += input_int
        else:  # input less than 0, so its a negative integer
            negative_counter += 1
            negative_inputs += input_int
    except ValueError:  # if can't get an int, throw user error
        print("The value must be an integer")

if positive_inputs == 0:
    print("There are no positive numbers!")
elif positive_inputs > 0:
    print("sum of positive values = {}".format(positive_inputs))
    pos_average = positive_inputs / positive_counter  # divide number by amount of times its been added to
    if pos_average.is_integer():  # if we can convert to an integer do it to remove any decimal point
        pos_average = int(pos_average)
        print("average of positive values = {}".format(pos_average))
    else:
        print("average of positive values = {}".format(pos_average))


if negative_inputs == 0:
    print("There are no negative numbers!")
elif negative_inputs < 0:
    print("sum of negative values = {}".format(negative_inputs))
    neg_average = negative_inputs / negative_counter   # divide number by amount of times its been added to
    if neg_average.is_integer():
        neg_average = int(neg_average)
        print("average of positive values = {}".format(neg_average))
    else:
        print("average of positive values = {}".format(neg_average))
