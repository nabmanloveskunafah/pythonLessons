# We shall find the hyptenuse of a 90 triangle  
import math

print("The formula is c = square root of a sqrd + b sqrd")

a = float(input("Choose a value for a: "))
b = float(input("Choose a value for b: "))
c = math.sqrt(a**2 + b**2)

print(f"The hypotenuse is {c:.2f}cm")