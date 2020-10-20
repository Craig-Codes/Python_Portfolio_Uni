# Prompt user to input an integer and output if odd or even

number = int(input("Input a positive integer: "))

if number % 2 == 0:
    #  If number is divisible by 2 with no remained it is even
    print("Number is even")
else:
    print("Number is odd")