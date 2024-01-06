subscription_cost = int(input())

snickers_price = subscription_cost - subscription_cost * 0.4
clothes_price = snickers_price - snickers_price * 0.2
ball_price = clothes_price * 0.25
accessories_price = ball_price * 0.2

total_cost = subscription_cost + snickers_price + clothes_price + ball_price + accessories_price

print(total_cost)
