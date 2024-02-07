brioche_count = int(input())
egg_boxes = int(input())
scones_kg = int(input())

eggs_price = egg_boxes * 4.35
egg_colorant_cost = egg_boxes * 12 * 0.15
eggs_cost = eggs_price + egg_colorant_cost
brioche_cost = brioche_count * 3.20
scones_cost = scones_kg * 5.40

total_cost = eggs_cost + brioche_cost + scones_cost

print(f"{total_cost:.2f}")
