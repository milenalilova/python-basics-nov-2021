destination = input()
travel_pack = input()
vip_discount = input()
days = int(input())
price = 0
is_incorrect = False
if days > 7:
    days -= 1

if destination == "Bansko" or destination == "Borovets":
    if travel_pack == "noEquipment":
        price = 80
        if vip_discount == "yes":
            price -= price * 0.05

    elif travel_pack == "withEquipment":
        price = 100
        if vip_discount == "yes":
            price -= price * 0.10


elif destination == "Varna" or destination == "Burgas":
    if travel_pack == "noBreakfast":
        price = 100
        if vip_discount == "yes":
            price -= price * 0.07
    elif travel_pack == "withBreakfast":
        price = 130
        if vip_discount == "yes":
            price -= price * 0.12

trip_cost = days * price

if days < 1:
    print("Days must be positive number!")
elif destination != "Bansko" and destination != "Borovets" \
        and destination != "Varna" and destination != "Burgas":
    print("Invalid input!")

elif travel_pack != "noEquipment" and travel_pack != "withEquipment" \
        and travel_pack != "noBreakfast" and travel_pack != "withBreakfast":
    print("Invalid input!")
else:
    print(f"The price is {trip_cost:.2f}lv! Have a nice time!")
