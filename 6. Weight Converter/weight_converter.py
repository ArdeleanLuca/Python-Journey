# The Weight Converter
weight = float(input("Weight: "))
unit = input("Kilograms(k) or Pounds?(p): ").upper()

if unit == "K":
    result = weight * 2.204
    print(f"{result:.2f}lbs")

elif unit == "K":
    result = weight / 2.204
    print(f"{result:.2f}kgs")

else:
    print("Error: Invalid unit!")
