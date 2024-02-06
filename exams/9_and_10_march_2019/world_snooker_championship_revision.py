round_type = input()
ticket_type = input()
tickets_count = int(input())
picture = input()
tickets_price = 0

if round_type == "Quarter final":
    if ticket_type == "Standard":
        tickets_price += tickets_count * 55.50

    elif ticket_type == "Premium":
        tickets_price += tickets_count * 105.20

    elif ticket_type == "VIP":
        tickets_price += tickets_count * 118.90

elif round_type == "Semi final":
    if ticket_type == "Standard":
        tickets_price += tickets_count * 75.88

    elif ticket_type == "Premium":
        tickets_price += tickets_count * 125.22

    elif ticket_type == "VIP":
        tickets_price += tickets_count * 300.40

elif round_type == "Final":
    if ticket_type == "Standard":
        tickets_price += tickets_count * 110.10

    elif ticket_type == "Premium":
        tickets_price += tickets_count * 160.66

    elif ticket_type == "VIP":
        tickets_price += tickets_count * 400

if 2500 < tickets_price <= 4000:
    tickets_price -= tickets_price * 0.1
    if picture == "Y":
        pictures_price = tickets_count * 40
        tickets_price += pictures_price

elif tickets_price > 4000:
    tickets_price -= tickets_price * 0.25

else:
    if picture == "Y":
        pictures_price = tickets_count * 40
        tickets_price += pictures_price

print(f"{tickets_price:.2f}")
