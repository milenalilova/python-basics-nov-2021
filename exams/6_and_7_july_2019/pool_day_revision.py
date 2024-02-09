from math import ceil

peoples_count = int(input())
entry_tax = float(input())
lounge_price = float(input())
shade_price = float(input())

lounge_count = ceil(peoples_count * 0.75)
shade_count = ceil(peoples_count / 2)

pool_cost = entry_tax * peoples_count + lounge_count * lounge_price + shade_count * shade_price

print(f"{pool_cost:.2f} lv.")
