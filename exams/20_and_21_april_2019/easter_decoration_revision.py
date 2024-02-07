customers_count = int(input())
total_bill = 0

for customers in range(customers_count):

    command = input()
    items_purchased = 0
    bill = 0

    while command != "Finish":

        if command == "basket":
            bill += 1.5
        elif command == "wreath":
            bill += 3.8
        elif command == "chocolate bunny":
            bill += 7
        items_purchased += 1

        command = input()

    if items_purchased % 2 == 0:
        bill -= bill * 0.2
    print(f"You purchased {items_purchased} items for {bill:.2f} leva.")
    total_bill += bill

average_bill = total_bill / customers_count

print(f"Average bill per client is: {average_bill:.2f} leva.")
