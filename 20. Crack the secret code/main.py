import random
print("Welcome to our mini game! Try to crack the secret code (1-100)!")
random_int = random.randint(1, 100)
attempts = 1

while True:
    num = int(input("Enter your guess: "))

    if num == random_int: 
        print(f"⭐ GREAT JOB! You cracked the code! The number was {random_int}!")
        print(f"Attempts: {attempts}")
        break

    elif abs(num - random_int) <= 5 and num != random_int: print("You're BURNING UP! (Very close): ")

    elif num < random_int: print("TOO LOW! Try a bigger number: ")

    else: print("TOO HIGH! Try a smaller number: ")
    attempts += 1
