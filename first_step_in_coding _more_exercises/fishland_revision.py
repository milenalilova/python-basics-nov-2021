mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
muscles_kg = int(input())

bonito_price = mackerel_price + 0.6 * mackerel_price
scad_price = sprat_price + 0.8 * sprat_price
muscles_price = 7.5

total_cost = bonito_kg * bonito_price + scad_kg * scad_price + muscles_kg * muscles_price

print(f"{total_cost:.2f}")
