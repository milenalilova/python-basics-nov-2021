import math

magnolias = int(input())
hyacinth = int(input())
roses = int(input())
cactus = int(input())
present_price = float(input())

magnolias_price = magnolias * 3.25
hyacinth_price = hyacinth * 4
roses_price = roses * 3.5
cactus_price = cactus * 8
total_order = magnolias_price + hyacinth_price + roses_price + cactus_price
profit = total_order - total_order * 0.05

if present_price <= profit:
    print(f"She is left with {math.floor(profit - present_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(present_price - profit)} leva.")
