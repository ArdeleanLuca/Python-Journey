foods = []
prices = []

while True:
    food = input("Food (q to finish): ")
    
    if food == "q": break

    price = float(input(f"Price for {food}: $"))

    foods.append(food)
    prices.append(price)

print("\n--- SHOPPING CART ---")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]}")

total = sum(prices)
print(f"\nTO PAY: ${total:.2f} ")
