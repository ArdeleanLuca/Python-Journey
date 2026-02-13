# Temperature Converter Pro
temperature = float(input("Temperature: "))
unit = input("Celsius (c) or Fahrenheit(f): ").upper()

if unit == "C":
    result = (temperature * 9/5) + 32
    if temperature <= 0:
        print(f"{result:.1f}F Warning: Freezing point!")
    elif temperature >= 100:
        print(f"{result:.1f} Warning: Boiling point!")
    else:
        print(f"{result:.1f}F")


elif unit == "F":
    result = (temperature - 32) * 5/9
    if temperature <= 32:
        print(f"{result:.1f}C Warning: Freezing point!")
    elif temperature >= 212:
        print(f"{result:.1f} Warning: Boiling point!")
    else:
        print(f"{result:.1f}C")

else:
    print("Wrong unit.")
    exit()
