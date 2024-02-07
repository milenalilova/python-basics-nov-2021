eggs_count = int(input())
eggs_sold = 0

command = input()

while command != "Close":

    quantity = int(input())
    if command == "Buy":
        if quantity > eggs_count:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_count}.")
            break
        else:
            eggs_count -= quantity
            eggs_sold += quantity

    elif command == "Fill":
        eggs_count += quantity

    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")
