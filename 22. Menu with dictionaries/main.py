menu = {
    "FRESH ORANGE": 26,
    "REDBULL": 24,
    "ESPRESSO": 16,
    "LATTE": 22,
    "ICED LATTE": 25
}

print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("-----------------------")

cart = []
total = 0

while True:
    drink = input("What drink would you like? (q to quit): ").upper()
    
    if drink == "Q":
        break
    
    if drink in menu:
        cart.append(drink)
        total += menu[drink]
        print(f"Added {drink} to your order!")
        print()
    else:
        print(f"Sorry, we don't have {drink} in our menu.")

print("\n" + "="*23)
print("       RECEIPT        ")
print("="*23)

for item in cart:
    print(f"{item:15}: ${menu[item]:.2f}")

print("-" * 23)
print(f"TOTAL TO PAY: ${total:.2f}")
print("="*23)
print("   Thanks for coming!  ")
