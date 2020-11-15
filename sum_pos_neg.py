# program prompts user to enter 10 integer values (pos or neg) and outputs sum of positives and sum of negatives

input_count = 0  # stores number of user inputs
positive_inputs = 0  # stores value of all positive integers
negative_inputs = 0  # stores value of all negative integers

while input_count < 10:  # loop 10 times - while loop chosen as loop may run over 10 times to account for input errors
    try:
        input_int = int(input("Enter a positive or negative integer value: "))
        input_count += 1  # add 1 to input count - once at 10 loop while breaks
        if input_int > 0:  # if input is greater than zero, its a positive integer
            positive_inputs += input_int
        else:  # input less than 0, so its a negative integer
            negative_inputs += input_int
    except ValueError:  # if can't get an int, throw user error
        print("The value must be an integer")

print("sum of positive values = {}".format(positive_inputs))
print("sum of negative values = {}".format(negative_inputs))

