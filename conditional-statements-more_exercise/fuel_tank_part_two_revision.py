fuel_type = input()
fuel_lt = float(input())
card_owned = input()

fuel_cost = 0

if fuel_type == "Gas":
    fuel_price = 0.93
    if card_owned == "Yes":
        fuel_price = 0.93 - 0.08
    fuel_cost = fuel_lt * fuel_price

elif fuel_type == "Gasoline":
    fuel_price = 2.22
    if card_owned == "Yes":
        fuel_price = 2.22 - 0.18
    fuel_cost = fuel_lt * fuel_price

elif fuel_type == "Diesel":
    fuel_price = 2.33
    if card_owned == "Yes":
        fuel_price = 2.33 - 0.12
    fuel_cost = fuel_lt * fuel_price

if 20 <= fuel_lt <= 25:
    fuel_cost = fuel_cost - fuel_cost * 0.08

elif fuel_lt > 25:
    fuel_cost = fuel_cost - fuel_cost * 0.10

print(f"{fuel_cost:.2f} lv.")
