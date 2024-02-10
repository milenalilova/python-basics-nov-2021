rent = float(input())

cake_price = rent * 0.2
drinks_price = cake_price - cake_price * 0.45
entertainer_cost = rent / 3

party_cost = rent + cake_price + drinks_price + entertainer_cost

print(party_cost)
