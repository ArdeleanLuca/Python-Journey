import math
# Circumference circle

#Circumference = 2pi * raza
#Circle Area = pi * radius^2

print("Area & Circumference of a circle")

radius = float(input("Radius: "))
Circumference = 2 * math.pi * radius
Area = math.pi * pow(radius, 2)

print(f"{Circumference:.2f}cm^2")
print(f"{Area:.2f}cm^2")

print("Hypotenuse of a right triangle")

#Hypotenuse right triangle = √c1^2 + c2^2
leg1 = float(input("Side A is: "))
leg2 = float(input("Side B is: "))
hypotenuse = math.sqrt(pow(leg1, 2) + pow(leg2, 2))
print(f"Side C is: {round(hypotenuse, 2)}")
