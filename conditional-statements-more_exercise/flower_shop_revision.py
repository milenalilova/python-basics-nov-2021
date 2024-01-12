from math import floor, ceil

magnolias_num = int(input())
hyacinth_num = int(input())
roses_num = int(input())
cactus_num = int(input())
present_price = int(input())

order_cost = magnolias_num * 3.25 + hyacinth_num * 4 + roses_num * 3.5 + cactus_num * 8
order_cost_net = order_cost - order_cost * 0.05

difference = abs(order_cost_net - present_price)

if present_price <= order_cost_net:
    print(f"She is left with {floor(difference)} leva.")

else:
    print(f"She will have to borrow {ceil(difference)} leva.")
