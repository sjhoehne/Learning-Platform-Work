# Calculate Hypotenuse
import math

a = float(input("Enter the length of Side a: "))
b = float(input("Enter the length of Side b: "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The Hypotenuse is {round(hypotenuse, 3)}cm")