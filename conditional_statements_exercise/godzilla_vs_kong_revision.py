budget = float(input())
extras_number = int(input())
costume_price = float(input())

decor_cost = budget * 0.1
costume_cost = extras_number * costume_price

if extras_number >= 150:
    costume_cost = costume_cost - costume_cost * 0.1

total_cost = decor_cost + costume_cost

if total_cost > budget:
    money_needed = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
