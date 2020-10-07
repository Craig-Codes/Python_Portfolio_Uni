# Calculating the distance travelled by an object moving at a constant velocity

u = float(input("initial velocity (m/s): "))
t = float(input("time taken (seconds): "))
a = float(input("acceleration (m/s\u00b2): "))

distance = (u * t) + (0.5 * (a * (t * t)))

print("The object travels {} meters".format(round(distance, 2)))
