joinery_count = int(input())
joinery_type = input()
delivery_option = input()
price = 0
is_invalid = False

if joinery_type == "90X130":
    price = 110
    if joinery_count < 10:
        is_invalid = True
    elif 10 <= joinery_count <= 30:
        price = price
    elif 30 < joinery_count <= 60:
        price -= price * 0.05

    elif joinery_count > 60:
        price -= price * 0.08

elif joinery_type == "100X150":
    price = 140
    if joinery_count < 10:
        is_invalid = True
    elif 10 <= joinery_count <= 40:
        price = price
    elif 40 < joinery_count <= 80:
        price -= price * 0.06

    elif joinery_count > 80:
        price -= price * 0.10

elif joinery_type == "130X180":
    price = 190
    if joinery_count < 10:
        is_invalid = True
    elif 10 <= joinery_count <= 20:
        price = price
    elif 20 < joinery_count <= 50:
        price -= price * 0.07

    elif joinery_count > 50:
        price -= price * 0.12

elif joinery_type == "200X300":
    price = 250
    if joinery_count < 10:
        is_invalid = True
    elif 10 <= joinery_count <= 25:
        price = price
    elif 25 < joinery_count <= 50:
        price -= price * 0.09

    elif joinery_count > 50:
        price -= price * 0.14

if joinery_count < 10:
    is_invalid = True

if not is_invalid:
    order_cost = joinery_count * price
    if delivery_option == "With delivery":
        order_cost += 60
    if joinery_count > 99:
        order_cost -= order_cost * 0.04

    print(f"{order_cost:.2f} BGN")
else:
    print("Invalid order")
