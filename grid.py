# Program to prompt the user to enter 2 numbers:
# one for number of columns and one for number of rows and outputs a grid of asterisks with the specified number of
# rows and columns

grid_rows = 0
grid_columns = 0

while not grid_rows and not grid_columns:  # ensure answers aren't left at zero
    try:
        grid_rows = int(input("Enter the number of rows: "))
        grid_columns = int(input("Enter the number of columns: "))
    except ValueError:
        print("You need to enter an integer values")

for row in range(grid_rows):
    column_length = 0  # start column length as zero for each iteration
    for column in range(grid_columns):
        column_length += 1  # add each column to the column_length variable
    print(column_length * "*")
