price_pens_pack = 5.80
price_markers_pack = 7.20
price_cleaning_product = 1.20

number_pens_pack = int(input())
number_markers_pack = int(input())
litres_cleaning_product = int(input())
discount_percentage = int(input())

total_price = number_pens_pack*price_pens_pack + number_markers_pack*price_markers_pack + \
              litres_cleaning_product*price_cleaning_product
discount = total_price*(discount_percentage/100)
discounted_price_to_pay = total_price - discount

print(discounted_price_to_pay)
