training_price = int(input())

snickers_price = training_price - 0.4*training_price
clothes_price = snickers_price - 0.2*snickers_price
ball_price = clothes_price*1/4
accessories_price = ball_price*1/5

total_cost = training_price + snickers_price + clothes_price + ball_price + accessories_price

print(total_cost)
