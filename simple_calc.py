# simple calculator allowing user to calculate two integers using different operators

try:
    input_one = int(input("Enter a positive integer: "))
    input_two = int(input("Enter a second positive integer: "))
    operator = str(input("Enter an operator as a string ( +, -, /, *): "))

    operators = ("+", "-", "/", "*")  # tuple stores valid operators
    if operator in operators:
        if operator == "+":
            print("Your sum is {} + {} and the answer is {}".format(input_one, input_two, input_one + input_two))
        if operator == "-":
            print("Your sum is {} - {} and the answer is {}".format(input_one, input_two, input_one - input_two))
        if operator == "/":
            print("Your sum is {} / {} and the answer is {}".format(input_one, input_two, input_one / input_two))
        if operator == "*":
            print("Your sum is {} * {} and the answer is {}".format(input_one, input_two, input_one * input_two))
    else:
        print("Ensure you select a valid operator")

except ValueError:
    print("Ensure you use an integer for the number inputs, and a character for operator input")