initials = []  # list stores all found initials

full_name = input("Enter you full name to get your initials: ")

name_list = full_name.split()  # get a list of the names

for name in name_list:  # loop through the names, picking out the first letter of each found name
    initials.append(name[0].upper())  # add the first letter of each name to the initials list

print("Your initials are:")
print(*initials, sep=".")  # display list without brackets, and separating each entry with a '.'
