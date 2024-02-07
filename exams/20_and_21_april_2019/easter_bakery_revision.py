flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_cartons = int(input())
yeast_packs = int(input())

sugar_price = flour_price - flour_price * 0.25
eggs_price = flour_price + flour_price * 0.1
yeast_price = sugar_price - sugar_price * 0.8

total_cost = flour_kg * flour_price + sugar_kg * sugar_price + eggs_cartons * eggs_price + yeast_packs * yeast_price

print(f"{total_cost:.2f}")
