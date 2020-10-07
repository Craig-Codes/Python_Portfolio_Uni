# Programme to calculate surface area and volume of a cuboid based on user input dimensions

width = int(input("Provide cuboid width: "))
height = int(input("Provide cuboid height: "))
length = int(input("Provide cuboid length: "))

surface_area = (2 * (length * height)) + (2 * (length * width)) + (2 * (height * width))
volume = width * height * length

print("The surface area is {}".format(surface_area))
print("The total volume is {}".format(volume))
