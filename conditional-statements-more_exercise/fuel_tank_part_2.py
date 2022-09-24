fuel_type = input()
quantity = float(input())
owns_card = input()

gasoline_price = quantity * 2.22
diesel_price = quantity * 2.33
gas_price = quantity * 0.93

if owns_card == "Yes":
    gasoline_price -= quantity * 0.18
    diesel_price -= quantity * 0.12
    gas_price -= quantity * 0.08
if 20 <= quantity <= 25:
    gasoline_price -= gasoline_price * 0.08
    diesel_price -= diesel_price * 0.08
    gas_price -= gas_price * 0.08
elif quantity > 25:
    gasoline_price -= gasoline_price * 0.1
    diesel_price -= diesel_price * 0.1
    gas_price -= gas_price * 0.1
if fuel_type == "Gasoline":
    print(f"{gasoline_price:.2f} lv.")
elif fuel_type == "Diesel":
    print(f'{diesel_price:.2f} lv.')
elif fuel_type == "Gas":
    print(f'{gas_price:.2f} lv.')

#
# if fuel_type == "Gasoline":
#     pass
# elif fuel_type == "Diesel":
#     pass
# elif fuel_type == "Gas":
#     pass