#Currency Converter
euro_exchange_rate = 5.0943
ron_exchange_rate = 1
question = int(input("EUR to RON(1) or RON to EUR?:(2) "))
if question == 1:
    eur = float(input("How much do you want to exchange from EUR to RON?: "))
    sum1 = eur * euro_exchange_rate
    print(f"{sum1:.3f}RON")
elif question == 2:
    ron = float(input("How much do you want to exchange from RON to EUR?: "))
    sum2 = ron / euro_exchange_rate
    print(f"{sum2:.3f}€")
else:
    print("At the moment, that's all we have!")
