budget = float(input())
extras_count = int(input())
costume_price = float(input())

decor_cost = budget * 0.1

if extras_count > 150:
    costume_price -= costume_price * 0.1

costume_cost = extras_count * costume_price
total_cost = decor_cost + costume_cost

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")
