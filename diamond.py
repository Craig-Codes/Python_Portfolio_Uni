while True:  # while no input
    try:
        width = int(input("Enter a width between 2 and 40 inclusive: "))
        if width > 40 or width < 2:
            print("Value must be between 2 and 40!")
        else:
            break  # break out of the loop as input is valid
    except ValueError:
        print("Ensure the input is an integer!")

# Top Loop
for i in range(width):  # loop up over each number, counting up till user input which is the max length
    # whole row length is made up of spaces on the left hand side and stars on the right (after the spaces)
    print(" " * (width - i - 1) + "* " * (i + 1))
    # space * width (minus current loop number, minus 1), plus the number of stars, which is the loop number plus 1

# Bottom Loop
# loop down over each number starting from one bellow the max width (top loop has already dealt with the longest line)
for j in range(width - 1):
    print(" " * (j + 1) + "* " * (width - j - 1))
    # reverse this line, doing the spaces first then using the width parameter to draw out correct number of stars.
