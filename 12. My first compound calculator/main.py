#Compound interest calculator
#P = float(input("Initial balance: "))
#while not P != 0:
#    P = float(input("Initial balance: "))
#print("Invalid amount!")
#P = float(input("Your Initial balance again is: "))
#r = float(input("Interest rate(%): "))
#while not r < 0:
#    print("Interest rate: ")
#    r = float(input("Interest rate(%): "))
#    break
#print("Invalid interest rate!")
#t = int(input("Number of time periods elapsed(in years): "))
#n = int(input("Compounding frequency(times per year): "))
#total = P * pow((1 + r/100/n), t)
#print(total)


p = float(input("Balanta initiala($): "))
while p > 0:
    r = float(input("Interest rate(%): "))
    while r > 0:
        t = float(input("Pe ce durata?(in ani): "))
        n = float(input("De cate ori pe an? "))
        total = float(p * pow((1 + r/100/n), t))
        break
    print()
    print("Invalid interest rate") if r < 0 else print("Just a moment...")
    break
print()
print("Invalid amount") if p < 0 else print(f"Balanta finala este {total:,.2f}$!")
print()
