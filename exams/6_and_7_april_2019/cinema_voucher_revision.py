voucher_value = int(input())

tickets_bought = 0
other_purchases_bought = 0

while voucher_value > 0:
    command = input()
    if command == "End":
        break
    purchase_value = 0

    if len(command) > 8:
        purchase_value += ord(command[0]) + ord(command[1])
        if purchase_value <= voucher_value:
            voucher_value -= purchase_value
            tickets_bought += 1

        else:
            break

    else:
        purchase_value += ord(command[0])
        if purchase_value <= voucher_value:
            voucher_value -= purchase_value
            other_purchases_bought += 1

        else:
            break

print(f"{tickets_bought}")
print(f"{other_purchases_bought}")
