expected_sum = int(input())

current_amount = 0
counter = 0
cash_payment = 0
cash_amount = 0
card_payment = 0
card_amount = 0

while True:
    command = input()
    if command == "End":
        break

    counter += 1
    current_transaction = int(command)

    if counter % 2 == 0:  # card
        if current_transaction < 10:
            print("Error in transaction!")
        else:
            current_amount += current_transaction
            card_payment += 1
            card_amount += current_transaction
            print("Product sold!")

    else:  # cash
        if current_transaction > 100:
            print("Error in transaction!")
        else:
            current_amount += current_transaction
            cash_payment += 1
            cash_amount += current_transaction
            print("Product sold!")

    if current_amount >= expected_sum:
        break

if current_amount >= expected_sum:
    average_cash_amount = cash_amount / cash_payment
    average_card_amount = card_amount / card_payment
    print(f"Average CS: {average_cash_amount:.2f}")
    print(f"Average CC: {average_card_amount:.2f}")

else:
    print("Failed to collect required money for charity.")
