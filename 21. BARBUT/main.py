import random
import time

player1name = input("First player: ").capitalize()
player2name = input("Second player: ").capitalize()

player1 = random.randint(1, 6)
player2 = random.randint(1, 6)

sum1 = 0
sum2 = 0
points1 = 0
points2 = 0
while True:
    if player1 == "q" or player2 == "q":
        break
    else:
        incontinuare = input("Vrei sa dai cu zarul 6-6? (Y / Q): ").upper()

        while incontinuare == "Y":
            time.sleep(1)

            points1 += player1
            points2 += player2

            print(f"{player1name}: {player1}")
            print(f"{player2name}: {player2}")

            player1 = random.randint(1, 6)
            player2 = random.randint(1, 6)
            
            incontinuare = input("Vrei sa dai cu zarul 6-6? (Y / Q): ").upper()
        break

print("-" * 20)
print("Rezultatul este: ")
time.sleep(3)
print(f"{player1name}: {points1}p")
print(f"{player2name}: {points2}p")
print()

if points1 > points2: print(f"Te-am spart {player2name}")
elif points1 == points2: print(f"Fmm egalitate intre noi")
else: print(f"Ești praf {player1name}, mai bagă o fise!")

