initials = []  # list stores all found initials

full_name = input("Enter full name to get your initials: ")

name_list = full_name.split()  # get a list of the names

for name in name_list:  # loop through the names, picking out the first letter of each found name
    substring = "-"  # we want to search for "-" to check for hyphenated names
    if substring in name:  # if the '-' is in the name entry
        index_pos = name.index(substring)  # get the index position of the hyphen
        index_pos += 1  # add one to index position to get the first character after the hyphen
        initials.append("{}-{}".format(name[0], name[index_pos]))
        # if we wanted to do this for triple hyphenated names, regex could be used to get multiple '-' positions
    else:
        initials.append(name[0].upper())  # add the first letter of each name to the initials list

print("Your initials are:")
print(*initials, sep=".")  # display list without brackets, and separating each entry with a '.'
