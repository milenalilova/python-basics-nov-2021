budget = float(input())
nights = int(input())
nights_price = float(input())
additional_cost_percentage = int(input())

additional_cost = budget * additional_cost_percentage / 100

if nights > 7:
    nights_price -= nights_price * 0.05

trip_cost = nights * nights_price + additional_cost

if budget >= trip_cost:
    print(f"Ivanovi will be left with {budget - trip_cost:.2f} leva after vacation.")
else:
    print(f"{trip_cost - budget:.2f} leva needed.")
