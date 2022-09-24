petar_budget = float(input())
videocard_number = int(input())
processor_number = int(input())

videocard_price = 250
videocard_sum = videocard_number * videocard_price
processor_price = videocard_sum * 0.35
ram_number = int(input())
ram_price = videocard_sum * 0.1

order_price = videocard_number * videocard_price + processor_number * processor_price + ram_number * ram_price

if videocard_number > processor_number:
    order_price = order_price - (order_price * 0.15)

if order_price <= petar_budget:
    print(f'You have {(petar_budget - order_price):.2f} leva left!')

else:
    print(f'Not enough money! You need {(order_price - petar_budget):.2f} leva more!')
    