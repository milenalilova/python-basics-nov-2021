age = int(input())
wash_machine_price = float(input())
toys_price = int(input())
toys_count = 0
sum_money = 0
money = 0

for birthdays in range(1, age + 1):
    if birthdays % 2 != 0:
        toys_count += 1
    else:
        money = money + 10
        sum_money = sum_money + money - 1

sold_toys_price = toys_count * toys_price
saved_money = sum_money + sold_toys_price
if saved_money >= wash_machine_price:
    print(f"Yes! {saved_money - wash_machine_price:.2f}")
else:
    print(f"No! {wash_machine_price - saved_money:.2f}")
