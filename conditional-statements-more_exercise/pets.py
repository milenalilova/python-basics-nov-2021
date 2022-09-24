import math

days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

total_food_needed_kg = (dog_food_kg + cat_food_kg + turtle_food_gr / 1000) * days

if total_food_needed_kg <= food_kg:
    print(f"{math.floor(food_kg - total_food_needed_kg)} kilos of food left.")
else:
    print(f"{math.ceil(total_food_needed_kg - food_kg)} more kilos of food are needed.")
