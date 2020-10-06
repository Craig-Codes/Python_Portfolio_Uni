# divide sweets equally amongst students, teacher keeps the remainder

sweets_in_packet = 40   # variable holding total number of sweets
student_number = 14     # variable holding number of students

sweets_per_student = int(sweets_in_packet / student_number)     # variable holding the amount of sweets per student
sweets_remaining = sweets_in_packet % student_number            # variable holding the remainder of sweets for teacher

print("Each student gets {} sweets".format(sweets_per_student))
print("The teacher get {} sweets".format(sweets_remaining))
