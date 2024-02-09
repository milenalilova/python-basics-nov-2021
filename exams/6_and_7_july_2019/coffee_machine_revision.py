hot_drink = input()
sugar = input()
hot_drinks_count = int(input())
price = 0

if hot_drink == "Espresso":
    if sugar == "Without":
        price = 0.90

    elif sugar == "Normal":
        price = 1

    elif sugar == "Extra":
        price = 1.20

elif hot_drink == "Cappuccino":
    if sugar == "Without":
        price = 1

    elif sugar == "Normal":
        price = 1.2

    elif sugar == "Extra":
        price = 1.60

elif hot_drink == "Tea":
    if sugar == "Without":
        price = 0.50

    elif sugar == "Normal":
        price = 0.60

    elif sugar == "Extra":
        price = 0.70

total_cost = hot_drinks_count * price
if sugar == "Without":
    total_cost -= total_cost * 0.35

if hot_drink == "Espresso" and hot_drinks_count > 5:
    total_cost -= total_cost * 0.25

if total_cost > 15:
    total_cost -= total_cost * 0.2

print(f"You bought {hot_drinks_count} cups of {hot_drink} for {total_cost:.2f} lv.")
