import math

vineyard_sq_meters = int(input())
grapes_kg_per_sqm = float(input())
wine_litres_needed = int(input())
workers_count = int(input())

wine_area = vineyard_sq_meters * 0.4
harvested_grapes = wine_area * grapes_kg_per_sqm
wine_litres_produced = harvested_grapes / 2.5
diff = abs(wine_litres_produced - wine_litres_needed)

if wine_litres_produced < wine_litres_needed:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
elif wine_litres_produced >= wine_litres_needed:
    print(f"Good harvest this year! Total wine: {math.floor(wine_litres_produced)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(diff / workers_count)} liters per person.")
