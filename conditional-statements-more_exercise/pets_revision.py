from math import floor, ceil

days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

turtle_food_kg = turtle_food_gr / 1000
total_food = (dog_food_kg + cat_food_kg + turtle_food_kg) * days
difference = abs(total_food - food_kg)

if total_food <= food_kg:
    print(f"{floor(difference)} kilos of food left.")

elif total_food > food_kg:
    print(f"{ceil(difference)} more kilos of food are needed.")
