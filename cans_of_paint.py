import math

# Calculate the amount of paint required to paint the walls (in full cans)
coverage_per_can = 5.1      # meters squared
wall_length = 40 + 40 + 30 + 30     # length of all the walls (meters)
wall_height = 3.4       # height of the walls (meters)
wall_area = wall_height * wall_length       # total area of the wall (meters squared)
# ceil() is used to ensure we get the largest integer equal to or greater than the input value ensuring enough paint
full_cans_required = math.ceil(wall_area / coverage_per_can)
print("1. {} cans will cover an area of {} meters squared".format(full_cans_required, int(wall_area)))

# Calculate the amount of full boxes of paint
cans_vs_width = 30 / 15     # cans can fit into the box 2 across
cans_vs_height = 60 / 30    # cans can fit into the boxes 2 stacked
cans_vs_length = math.floor(35 / 15)    # cans can fit into the boxes 2 length (with a little space spare)
# floor() is used to ensure we get the largest integer equal to or less than the input value ensuring cans fit in box
cans_per_box = cans_vs_width * cans_vs_height * cans_vs_length
boxes = math.floor(full_cans_required / cans_per_box)
loose_cans = full_cans_required % cans_per_box
print("2. {} boxes will be given to the customer to carry the cans".format(boxes))
print("3. The number of loose cans is {}".format(int(loose_cans)))
