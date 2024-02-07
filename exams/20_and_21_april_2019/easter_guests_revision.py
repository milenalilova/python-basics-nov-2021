from math import ceil

guests_count = int(input())
budget = int(input())

brioche_needed = ceil(guests_count / 3)
eggs_needed = guests_count * 2

brioche_cost = brioche_needed * 4
eggs_cost = eggs_needed * 0.45
total_cost = brioche_cost + eggs_cost

if budget >= total_cost:
    print(f"Lyubo bought {brioche_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {budget - total_cost:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total_cost - budget:.2f} lv. more.")
