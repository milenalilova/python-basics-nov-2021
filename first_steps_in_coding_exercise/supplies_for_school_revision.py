pens_price = 5.80
markers_price = 7.20
product_price = 1.20

packs_pens = int(input())
packs_markers = int(input())
litres_product = int(input())
discount_percent = int(input())

total_cost = packs_pens * pens_price + packs_markers * markers_price + litres_product * product_price
discount = total_cost * (discount_percent / 100)

final_price = total_cost - discount

print(final_price)
