city = input()
quantity = float(input())
commission = 0
condition = False

if city == "Sofia":
    if 0 <= quantity <= 500:
        commission = 0.05
    elif 500 < quantity <= 1000:
        commission = 0.07
    elif 1000 < quantity <= 10000:
        commission = 0.08
    elif quantity > 10000:
        commission = 0.12
    else:
        condition = True

elif city == "Varna":
    if 0 <= quantity <= 500:
        commission = 0.045
    elif 500 < quantity <= 1000:
        commission = 0.075
    elif 1000 < quantity <= 10000:
        commission = 0.10
    elif quantity > 10000:
        commission = 0.13
    else:
        condition = True

elif city == "Plovdiv":
    if 0 <= quantity <= 500:
        commission = 0.055
    elif 500 < quantity <= 1000:
        commission = 0.08
    elif 1000 < quantity <= 10000:
        commission = 0.12
    elif quantity > 10000:
        commission = 0.145
    else:
        condition = True

else:
    condition = True

commission = quantity * commission

if condition:
    print("error")
else:
    print(f"{commission:.2f}")
