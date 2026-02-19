print()
name = input("Hey! What is your name?: ")
while True:
    weight = float(input("Please insert your weight(kg): "))
    if weight <= 0:
        print("Invalid weight")
    else:
        break

while True:
    height = float(input("Please insert your height(cm): "))
    if not height > 0:
        print("Invalid height")
    else:
        break

while True:
    age = int(input("Please insert your age: "))
    if not age > 0:
        print("Invalid age!")
    else:
        break

#YAY AM INVATAT UN CONCEPT NOU 
gender_box = "M", "F"

while True:
    gender = input("Please insert your gender(M / F): ").upper()
    if gender not in gender_box:
        print("Invalid gender!")
    else:
        break

# Calculations
man_bmr = float(10 * weight + 6.25 * height - 5 * age + 5)
female_bmr = float(10 * weight + 6.25 * height - 5 * age -161)

print()
print("Please choose between 1,2 or 3 based off your activity: ")
print("1. Sedentary (little or no exercise)")
print("2. Moderate (exercise 3-5 days/week)")
print("3. Active (hard exercise 6-7 days/week)")
activity = int(input())

while activity > 0 and activity <= 3:
    if activity == 1:
        m1 = man_bmr * 1.2
        f1 = female_bmr * 1.2
        break

    elif activity == 2:
        m2 = man_bmr * 1.55
        f2 = female_bmr * 1.55
        break

    elif activity == 3:
        m3 = man_bmr * 1.9
        f3 =female_bmr * 1.9
        break

print()
print("--- USER HEALTH PROFILE ---")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Weight: {weight}kg")
print(f"Height: {height}cm")
print(f"Age: {age}")
print(f"Activity level: {activity}")

print()
print("Calculation Results:")

if gender == "M":
    print(f"Your BMR: {man_bmr:,.1f}kcal")
else:
    print(f"Your BMR is: {female_bmr:,.1f}kcal")


while gender == "M":
    if activity == 1:
        print(f"Your Daily Calories are: {m1:,.1f}kcal")
        break
    elif activity == 2:
        print(f"Your Daily Calories are: {m2:,.1f}kcal")
        break
    elif activity == 3:
        print(f"Your Daily Calories are: {m3:,.1f}kcal")
        break


while gender == "F":
    if activity == 1:
        print(f"Your Daily Calories are: {f1:,.1f}kcal")
        break
    elif activity == 2:
        print(f"Your Daily Calories are: {f2:,.1f}kcal")
        break
    elif activity == 3:
        print(f"Your Daily Calories are: {f3:,.1f}kcal")
        break
print()
future_question = input("Do you want to lose or gain weight?(L/G):")

while future_question == "L" and gender == "M":
    if activity == 1:
        print(f"You should consume: {m1 - 500:,.1f}kcal")
        print()
        break
    elif activity == 2:
        print(f"You should consume: {m2 - 500:,.1f}kcal")
        print()
        break
    elif activity == 3:
        print(f"You should consume: {m3 - 500:,.1f}kcal")
        print()
        break

while future_question == "G" and gender == "M":
    if activity == 1:
        print(f"You should consume: {m1 + 500:.1f}kcal")
        print()
        break
    elif activity == 2:
        print(f"You should consume: {m2 + 500:.1f}kcal")
        print()
        break
    elif activity == 3:
        print(f"You should consume: {m3 + 500:.1f}kcal")
        print()
        break

while future_question == "L" and gender == "F":
    if activity == 1:
        print(f"You should consume: {f1 - 500:.1f}kcal")
        print()
        break
    elif activity == 2:
        print(f"You should consume: {f2 - 500:.1f}kcal")
        print()
        break
    elif activity == 3:
        print(f"You should consume: {f3 - 500:.1f}kcal")
        print()
        break

while future_question == "G" and gender == "F":
    if activity == 1:
        print(f"You should consume: {f1 + 500:.1f}kcal")
        print()
        break
    elif activity == 2:
        print(f"You should consume: {f2 + 500:.1f}kcal")
        print()
        break
    elif activity == 3:
        print(f"You should consume: {f3 + 500:.1f}kcal")
        print()
        break
