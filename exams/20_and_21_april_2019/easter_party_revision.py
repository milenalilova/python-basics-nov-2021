guest_count = int(input())
dinner_price = float(input())
budget = float(input())

if 10 <= guest_count <= 15:
    dinner_price -= dinner_price * 0.15

elif 15 < guest_count <= 20:
    dinner_price -= dinner_price * 0.20

elif guest_count > 20:
    dinner_price -= dinner_price * 0.25

cake_price = budget * 0.1

total_cost = guest_count * dinner_price + cake_price

if budget >= total_cost:
    print(f"It is party time! {budget - total_cost:.2f} leva left.")
else:
    print(f"No party! {total_cost - budget:.2f} leva needed.")
