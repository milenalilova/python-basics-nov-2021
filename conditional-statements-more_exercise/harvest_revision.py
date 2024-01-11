from math import floor, ceil

vineyard_sqm = int(input())
grapes_per_sqm = float(input())
wine_needed_litres = int(input())
workers_count = float(input())

wine_area = vineyard_sqm * 0.4
grapes_produced = wine_area * grapes_per_sqm
wine_produced = grapes_produced / 2.5

if wine_produced < wine_needed_litres:
    print(f"It will be a tough winter! More {floor(wine_needed_litres - wine_produced)} liters wine needed.")

else:
    wine_left = wine_produced - wine_needed_litres
    wine_per_worker = wine_left / workers_count
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_per_worker)} liters per person.")
