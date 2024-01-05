square_meters = float(input())
price_per_sq_meter = 7.61
total_cost = square_meters * price_per_sq_meter
discount = total_cost * 0.18

final_cost = total_cost - discount

print(f'The final price is: {final_cost} lv.')
print(f'The discount is: {discount} lv.')
