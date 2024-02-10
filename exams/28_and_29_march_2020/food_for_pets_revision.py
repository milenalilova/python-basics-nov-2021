days = int(input())
food_amount = float(input())

dogs_amount = 0
cats_amount = 0
biscuits = 0

for day in range(1, days + 1):
    dogs_daily_amount = int(input())
    cats_daily_amount = int(input())
    dogs_amount += dogs_daily_amount
    cats_amount += cats_daily_amount

    if day % 3 == 0:
        daily_food_amount = dogs_daily_amount + cats_daily_amount
        biscuits += daily_food_amount * 0.1

food_eaten = dogs_amount + cats_amount
food_eaten_percentage = food_eaten / food_amount * 100
dog_food_percentage = dogs_amount / food_eaten * 100
cat_food_percentage = cats_amount / food_eaten * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{food_eaten_percentage:.2f}% of the food has been eaten.")
print(f"{dog_food_percentage:.2f}% eaten from the dog.")
print(f"{cat_food_percentage:.2f}% eaten from the cat.")
