import random

# Dice Art Dictionary
dices = {
    1: ("┏━━━━━━━┓", "┃       ┃", "┃   ●   ┃", "┃       ┃", "┗━━━━━━━┛"),
    2: ("┏━━━━━━━┓", "┃ ●     ┃", "┃       ┃", "┃     ● ┃", "┗━━━━━━━┛"),
    3: ("┏━━━━━━━┓", "┃ ●     ┃", "┃   ●   ┃", "┃     ● ┃", "┗━━━━━━━┛"),
    4: ("┏━━━━━━━┓", "┃ ●   ● ┃", "┃       ┃", "┃ ●   ● ┃", "┗━━━━━━━┛"),
    5: ("┏━━━━━━━┓", "┃ ●   ● ┃", "┃   ●   ┃", "┃ ●   ● ┃", "┗━━━━━━━┛"),
    6: ("┏━━━━━━━┓", "┃ ●   ● ┃", "┃ ●   ● ┃", "┃ ●   ● ┃", "┗━━━━━━━┛")
}

is_running = True

while is_running:
    question = input("Press ENTER to roll (q to quit): ").lower()

    if question == "":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"\nPlayer 1 rolled {dice1}:")
        for row in dices[dice1]:
            print(row)

        input("\nPress ENTER for Player 2...")

        print(f"Player 2 rolled {dice2}:")
        for row in dices[dice2]:
            print(row)

        print("-" * 10)
        if dice1 > dice2:
            print("RESULT: Player 1 wins!")
        elif dice1 < dice2:
            print("RESULT: Player 2 wins!")
        else:
            print("RESULT: It's a draw!")
        print("-" * 10)

    elif question == "q":
        print("Thanks for playing!")
        is_running = False
