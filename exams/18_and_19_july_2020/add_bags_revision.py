luggage_over_20_price = float(input())
luggage_weight = float(input())
days_to_flight = int(input())
luggage_count = int(input())

luggage_price = 0

if luggage_weight < 10:
    luggage_price = luggage_over_20_price * 0.2

elif 10 <= luggage_weight <= 20:
    luggage_price = luggage_over_20_price * 0.5

elif luggage_weight > 20:
    luggage_price = luggage_over_20_price

if days_to_flight < 7:
    luggage_price += luggage_price * 0.4

elif 7 <= days_to_flight <= 30:
    luggage_price += luggage_price * 0.15

elif days_to_flight > 30:
    luggage_price += luggage_price * 0.1

final_price = luggage_count * luggage_price

print(f"The total price of bags is: {final_price:.2f} lv.")
