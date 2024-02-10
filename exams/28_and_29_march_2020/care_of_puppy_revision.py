food_amount_kg = int(input())
food_amount_gr = food_amount_kg * 1000
food_eaten = 0

command = input()

while command != "Adopted":
    daily_food_eaten_gr = int(command)
    food_eaten += daily_food_eaten_gr

    command = input()

if food_amount_gr >= food_eaten:
    food_left = food_amount_gr - food_eaten
    print(f"Food is enough! Leftovers: {food_left} grams.")
else:
    food_needed = food_eaten - food_amount_gr
    print(f"Food is not enough. You need {food_needed} grams more.")
