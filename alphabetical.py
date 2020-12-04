string_list = []  # list to hold the string inputs


# function gets user input and assigns it to the string_list
def string_input():
    user_input = str(input("Enter a string: "))
    string_list.append(user_input)


# function builds the string list by calling the string_input function 5 times
def list_builder():
    for i in range(5):  # loop through 5 times, requesting 5 inputs
        string_input()


list_builder()  # get the user input
string_list.sort()  # use inbuilt sort method to sort alphabetically
print(string_list)  # print the sorted list

