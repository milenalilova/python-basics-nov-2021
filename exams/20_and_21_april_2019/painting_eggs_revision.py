egg_size = input()
egg_colour = input()
eggs_count = int(input())
price = 0

if egg_size == "Large":
    if egg_colour == "Red":
        price = 16

    elif egg_colour == "Green":
        price = 12

    elif egg_colour == "Yellow":
        price = 9

elif egg_size == "Medium":
    if egg_colour == "Red":
        price = 13

    elif egg_colour == "Green":
        price = 9

    elif egg_colour == "Yellow":
        price = 7

elif egg_size == "Small":
    if egg_colour == "Red":
        price = 9

    elif egg_colour == "Green":
        price = 8

    elif egg_colour == "Yellow":
        price = 5

eggs_sales = eggs_count * price
production_cost = eggs_sales * 0.35
profit = eggs_sales - production_cost

print(f"{profit:.2f} leva.")
