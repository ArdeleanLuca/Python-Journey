# BMR Calculator
name = input("What's your name?: ").upper()
while True:
    weight = float(input("Weight(kg): "))
    if not weight > 0: print("Invalid weight!")
    else: break

while True:
    height = float(input("Height(cm): "))
    if not height > 0: print("Invalid height!")
    else: break

while True:
    age = int(input("Age: "))
    if not age > 0: print("Invalid age!")
    else: break

gender = input("Gender(M / F): ").upper()
if gender == "M": bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
else: bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

multipliers = {"1": 1.2, "2":1.375, "3":1.55, "4":1.725, "5":1.9}
choice = input("\n1. Sedentary | 2. Lightly active | 3. Moderately Active | 4.Very Active | 5. Extra Active: ")
active_multiplier = multipliers[choice]
daily_calories = bmr * active_multiplier

goal = input("What's your goal? To Lose or Gain weight? (L / G): ")
if goal == "L": goal_calories = daily_calories - 500
else: goal_calories = daily_calories + 500

print(f"---{name} Profile---")
print(f"Your BMR is: {bmr}")
print(f"Your daily calories are: {daily_calories}")
print(f"Your goal calories are: {goal_calories}")


