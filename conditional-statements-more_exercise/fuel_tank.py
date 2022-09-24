fuel_type = input()
litres_fuel = float(input())

if fuel_type == "Diesel":
    if litres_fuel >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif fuel_type == "Gasoline":
    if litres_fuel >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif fuel_type == "Gas":
    if litres_fuel >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print(f"Invalid fuel!")

