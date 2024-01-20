age = int(input())
washer_price = float(input())
toy_price = int(input())
money = 0
presents_sum = 0
toys_count = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money = money + 10
        presents_sum = presents_sum + money - 1
    else:
        toys_count += 1

sold_sum = toys_count * toy_price
presents_sum += sold_sum

difference = abs(washer_price - presents_sum)

if presents_sum >= washer_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
