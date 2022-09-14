nylon_price = 1.50
paint_price = 14.50
dissolvent_price = 5.00

nylon_quantity = int(input())
paint_quantity = int(input())
dissolvent_quantity = int(input())
working_hours = int(input())

total_price_materials = (nylon_quantity + 2)*nylon_price + \
                        (paint_quantity + paint_quantity*0.1)*paint_price + \
                        dissolvent_quantity*dissolvent_price + 0.40
labour_cost = (total_price_materials*0.3)*working_hours
total_cost = total_price_materials + labour_cost

print(total_cost)


