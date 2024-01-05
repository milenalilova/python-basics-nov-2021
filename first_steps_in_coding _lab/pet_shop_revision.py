dog_food_quantity = int(input())
cat_food_quantity = int(input())
dog_food_price = 2.5
cat_food_price = 4

dog_food_cost = dog_food_quantity * dog_food_price
cat_food_cost = cat_food_quantity * cat_food_price

final_food_cost = dog_food_cost + cat_food_cost

print(f'{final_food_cost} lv.')
