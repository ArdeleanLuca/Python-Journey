import random

print()
print("=" * 40)
print("WELCOME TO ROCK, PAPER, SCISSORS!")
print("=" * 40)

options = ("rock", "paper", "scissors")

while True:
    print("\n" + "-" * 20)
    player = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
    
    if player == "q":
        print("\nThanks for playing! Final scores recorded.")
        break

    if player not in options:
        print("❌ Invalid choice! Please type 'rock', 'paper', or 'scissors'.")
        continue

    computer = random.choice(options)

    print(f"\nYour Move:     {player.capitalize()}")
    print(f"Computer Move: {computer.capitalize()}")
    print("-" * 20)

    # Logic to determine the winner
    if player == computer:
        print("RESULT: It's a tie!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("✨ RESULT: YOU WON! Congratulations! ✨")
        
    else:
        print("RESULT: COMPUTER WINS! Better luck next time.")

print("=" * 40)
