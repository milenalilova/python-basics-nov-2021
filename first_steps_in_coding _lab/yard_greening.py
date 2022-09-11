square_meters_for_greening = float(input())
price_per_square_meter = 7.61
total_price_for_greening = square_meters_for_greening * price_per_square_meter
discount = 0.18 * total_price_for_greening
final_price = total_price_for_greening - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
