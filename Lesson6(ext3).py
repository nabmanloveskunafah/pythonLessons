import math

print("Today we will find a circumference of a circle")
radius = float(input("Choose a radius:"))

Circumference = 2 * math.pi * radius

print(f"the circumference is {Circumference:.2f}cm")

print("Now we will find the area of a circle")

radius2 = float(input("Choose a new radius: "))

Area = math.pi * radius2 ** 2

print(f"The area is {Area:.2f}cm^2")



