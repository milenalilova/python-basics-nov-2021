subscription_fee = int(input())

snickers_price = subscription_fee - subscription_fee * 0.4
clothes_price = snickers_price - snickers_price * 0.2
ball_price = clothes_price / 4
accessories_price = ball_price / 5

expenses = subscription_fee + snickers_price + clothes_price + ball_price + accessories_price

print(f"{expenses:.2f}")
