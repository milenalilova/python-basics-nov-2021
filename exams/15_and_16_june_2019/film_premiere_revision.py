movie_name = input()
menu_pack = input()
tickets_count = int(input())
price = 0

if movie_name == "John Wick":
    if menu_pack == "Drink":
        price = 12

    elif menu_pack == "Popcorn":
        price = 15

    elif menu_pack == "Menu":
        price = 19

elif movie_name == "Star Wars":
    if menu_pack == "Drink":
        price = 18

    elif menu_pack == "Popcorn":
        price = 25

    elif menu_pack == "Menu":
        price = 30

    if tickets_count >= 4:
        price -= price * 0.3

elif movie_name == "Jumanji":
    if menu_pack == "Drink":
        price = 9

    elif menu_pack == "Popcorn":
        price = 11

    elif menu_pack == "Menu":
        price = 14

    if tickets_count == 2:
        price -= price * 0.15

sales = tickets_count * price

print(f"Your bill is {sales:.2f} leva.")
