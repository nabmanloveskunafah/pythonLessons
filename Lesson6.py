Chocolate = 10
Crisps = 4
Fruit = 2
Nuts = 5
Drinks = 3

# Addition, Subtraction, Division, Multiplication, Exponentiation
Chocolate += 1
Crisps -= 2
Fruit /= 4
Nuts *= 5
Drinks **= 3

# Modulus: The remainder after a number is divided
## 11 %2 = 1. This is because 11/ 2 = 5 with a remainder of 1 
### % in this case is the Modulus operator (division w/ remainder)
remainder = Chocolate % 2

print("...")
print (f"Chocolate: {Chocolate}")
print (f"Crisps: {Crisps}")
print (f"Fruit: {Fruit}")
print (f"Nuts: {Nuts}")
print (f"Drinks {Drinks}")
print (f"{remainder} of Choc")

