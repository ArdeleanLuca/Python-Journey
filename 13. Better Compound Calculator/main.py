while True:
    p = float(input("Initial balance($): "))
    if not p > 0:
        print("Your balance needs to be grater than 0!")
    else:
        break

while True:
    r = float(input("Interest Rate: "))
    if r < 0:
        print("Your interest rate must be above 0!")
    else:
        break

while True:
    n = float(input("Compounding frequency (times per year): "))
    if n <= 0:
        print("Frequency must be greater than 0!")
    else:
        break

while True:
    t = float(input("Duration (years): "))
    if t <= 0:
        print("Time must be greater than 0!")
    else:
        break

total = p * pow((1 + (r/100) / n), (n * t))
print(f"\nYour final balance will be: ${total:,.2f}!")
