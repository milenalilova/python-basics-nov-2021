plastic_price = 1.5
paint_price = 14.5
solvent_price = 5
bags_cost = 0.4

plastic_needed = int(input())
paint_needed = int(input())
solvent_quantity = int(input())
men_hours = int(input())

paint_quantity = paint_needed + paint_needed * 0.1
plastic_quantity = plastic_needed + 2

materials_cost = plastic_quantity * plastic_price + paint_quantity * paint_price + solvent_quantity * solvent_price + bags_cost
men_hours_price = materials_cost * 0.3
labour_cost = men_hours * men_hours_price
total_cost = materials_cost + labour_cost

print(total_cost)
