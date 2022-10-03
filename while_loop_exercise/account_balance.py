command = input()
balance = 0

while command != "NoMoreMoney":
    amount = float(command)
    if amount < 0:
        print("Invalid operation!")
        break
        # print(f"Total: {balance}")
    balance += amount
    print(f"Increase: {amount:.2f}")
    command = input()

print(f"Total: {balance:.2f}")
